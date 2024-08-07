/*
THIS IS A GENERATED/BUNDLED FILE BY ESBUILD
if you want to view the source, please visit the github repository of this plugin
*/

var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => GraphBannerPlugin
});
module.exports = __toCommonJS(main_exports);
var import_remote = require("@electron/remote");
var import_obsidian = require("obsidian");
var _GraphBannerPlugin = class _GraphBannerPlugin extends import_obsidian.Plugin {
  constructor() {
    super(...arguments);
    this.unloadListeners = [];
    this.graphNode = null;
    this.graphWindowID = null;
  }
  async onload() {
    console.log("Loading GraphBannerPlugin");
    this.app.workspace.trigger("parse-style-settings");
    if (import_obsidian.Platform.isDesktopApp) {
      const hideGraphWindow = () => {
        const obsidianWindows = import_remote.BrowserWindow.getAllWindows();
        const hiddenGraphWindow = obsidianWindows.find(
          (win) => win.id === this.graphWindowID && !win.isVisible()
        );
        if (hiddenGraphWindow) return;
        const graphWindow = obsidianWindows.find(
          (win) => win.getTitle().startsWith("Graph")
        );
        if (!graphWindow) return;
        this.graphWindowID = graphWindow.id;
        graphWindow.hide();
        this.unloadListeners.push(() => {
          graphWindow.closable && graphWindow.close();
        });
      };
      this.addCommand({
        id: "hide-window",
        name: "Hide the local window used for banner",
        callback: hideGraphWindow
      });
      const showGraphWindows = () => {
        const obsidianWindows = import_remote.BrowserWindow.getAllWindows();
        for (const win of obsidianWindows) {
          !win.isVisible() && win.show();
        }
      };
      this.addCommand({
        id: "show-hidden-windows",
        name: "Show hidden local graph windows",
        callback: showGraphWindows
      });
      this.registerEvent(
        this.app.workspace.on("window-open", async (workspaceWindow) => {
          if (workspaceWindow.getContainer() instanceof import_obsidian.WorkspaceRoot) return;
          await new Promise((resolve) => setTimeout(resolve, 200));
          hideGraphWindow();
        })
      );
    }
    this.registerEvent(
      this.app.workspace.on("file-open", async (file) => {
        if (!file || file.extension !== "md") return;
        const fileView = await this.tryUntilNonNull(
          () => this.app.workspace.getActiveViewOfType(import_obsidian.MarkdownView)
        );
        if (fileView.file !== file) {
          throw new Error("Failed to get file view");
        }
        let graphLeaf = this.getGraphLeaf();
        if (!graphLeaf) {
          graphLeaf = await this.openNewGraphLeaf();
          if (import_obsidian.Platform.isDesktopApp) {
            this.app.workspace.moveLeafToPopout(graphLeaf);
          }
          this.app.workspace.setActiveLeaf(fileView.leaf);
        }
        if (!this.graphNode) {
          const graphNode2 = graphLeaf.view.containerEl.getElementsByClassName("view-content").item(0);
          if (!graphNode2) {
            throw new Error("Failed to get graph node");
          }
          graphNode2.addClass(_GraphBannerPlugin.graphBannerNodeClass);
          this.graphNode = graphNode2;
        }
        const graphNode = await this.tryUntilNonNull(() => this.graphNode);
        if (fileView.containerEl.contains(graphNode)) {
          return;
        }
        const graphControls = graphNode.getElementsByClassName("graph-controls").item(0);
        graphControls == null ? void 0 : graphControls.toggleClass("is-close", true);
        const noteHeader = fileView.containerEl.getElementsByClassName("inline-title").item(0);
        if (!(noteHeader == null ? void 0 : noteHeader.parentElement) || !(noteHeader == null ? void 0 : noteHeader.nextSibling)) {
          throw new Error("Failed to get note header");
        }
        noteHeader.parentElement.insertBefore(
          graphNode,
          noteHeader.nextSibling
        );
        this.registerEvent(
          this.app.workspace.on("layout-change", async () => {
            const fileView2 = this.app.workspace.getActiveViewOfType(import_obsidian.MarkdownView);
            if (!fileView2) return;
            const noteHeader2 = await this.tryUntilNonNull(
              () => fileView2.containerEl.getElementsByClassName("inline-title").item(0)
            );
            if (!noteHeader2.parentElement || !noteHeader2.nextSibling) {
              throw new Error("Failed to get note header");
            }
            if (noteHeader2.parentElement.contains(graphNode)) return;
            noteHeader2.parentElement.insertBefore(
              graphNode,
              noteHeader2.nextSibling
            );
          })
        );
      })
    );
  }
  async onunload() {
    var _a;
    console.log("Unloading GraphBannerPlugin");
    (_a = this.graphNode) == null ? void 0 : _a.removeClass(_GraphBannerPlugin.graphBannerNodeClass);
    this.graphNode = null;
    for (const unloadCallback of this.unloadListeners) {
      unloadCallback();
    }
  }
  async tryUntilNonNull(f, interval = 200, maxCount = 10) {
    for (let i = 0; i < maxCount; i++) {
      const result = f();
      if (result) return result;
      await new Promise((resolve) => setTimeout(resolve, interval));
    }
    throw new Error(`Failed to get result: ${f.toString().slice(0, 100)}...`);
  }
  getGraphLeaf() {
    return this.app.workspace.getLeavesOfType("localgraph").find(
      (leaf) => leaf.view.containerEl.getElementsByClassName(
        _GraphBannerPlugin.graphBannerNodeClass
      )
    );
  }
  async openNewGraphLeaf() {
    await this.app.commands.executeCommandById("graph:open-local");
    const graphLeaf = await this.tryUntilNonNull(() => this.getGraphLeaf());
    graphLeaf.setGroup("graph-banner");
    return graphLeaf;
  }
};
_GraphBannerPlugin.graphBannerNodeClass = "graph-banner-content";
var GraphBannerPlugin = _GraphBannerPlugin;
