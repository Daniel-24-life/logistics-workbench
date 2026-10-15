<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/cover-dark.svg" />
  <img src="docs/assets/cover-light.svg" alt="logistics-workbench" width="1280" />
</picture>

# 航序 · 跨境物流 AI 运营协同工作台

[完整作品目录](https://github.com/Daniel-24-life/AIfile)

一个可独立运行的公开产品演示：以虚构跨境物流记录串联异常识别、固定 AI 建议、人工审核、调度任务与客户状态视图。

![航序工作台桌面截图](docs/assets/workbench-desktop.png)

## 本地运行

需要 Python 3.11+。在仓库根目录运行：

```powershell
python -m http.server 4181 --bind 127.0.0.1 --directory dist
```

然后打开 <http://127.0.0.1:4181>。

v1.1 将异常队列作为主区域，详情按事实、缺口和建议展开。编辑窗口支持 Tab、Shift+Tab 与 Escape，关闭后返回触发控件。仅提供本地运行，不新增在线托管。

[界面审查](docs/UI_AUDIT.md) · [本轮界面验证](docs/UI_QA.md)

运行 Node.js 22+ 的无依赖策略测试：

```powershell
node --test tests/policy.test.cjs
node --check dist/app.js
node --check dist/policy.js
```

## 演示路径

1. 在异常中心打开 `EX-1042`，查看事实、缺失信息与固定建议。
2. 使用“物流操作”审核建议并创建调度任务。
3. 切换为“调度人员”，将任务推进至执行、提交完成证据和关闭。
4. 切换为“客户用户”，查看过滤后的状态页面。
5. 以可审核角色打开过期的 `EX-1039`：直接采纳仍会被阻止。
6. 查看数据接入、字段映射、终端适配和“恢复初始数据”。

## 公开边界

- 所有运单、身份、费用、集成健康度、时间与 AI 建议均为固定合成数据。
- 角色选择器是产品交互演示，不是身份认证、授权系统或租户隔离；浏览器源码可见全部样例数据。
- “提交完成证据”和“验证并回写”按钮仅改变内存中的演示状态，既不上传文件，也不执行独立证据核验。
- 刷新页面会重置业务状态；没有后端、外部 API、模型调用或持久审计库。

生产化仍需服务端身份与权限、按客户过滤的响应、可追溯事件、真实证据引用和独立校验。详见 [参考指南](docs/reference-guide.md)、[架构说明](docs/architecture.md) 与 [验证记录](docs/VERIFICATION.md)。

## 仓库导航

| 路径 | 内容 |
| --- | --- |
| [dist/index.html](dist/index.html) | 静态页面入口、角色选择与详情面板。 |
| [dist/app.js](dist/app.js) | 合成数据、异常/任务流、客户视图和本地审计展示。 |
| [dist/policy.js](dist/policy.js) | 浏览器与 Node 测试共享的策略检查。 |
| [tests/policy.test.cjs](tests/policy.test.cjs) | 5 个既有的策略边界测试。 |
| [docs/reference-guide.md](docs/reference-guide.md) | 角色、状态机与模拟边界。 |
| [docs/architecture.md](docs/architecture.md) | 演示实现与生产所需能力的对照。 |
| [docs/SOURCE_READING_GUIDE.md](docs/SOURCE_READING_GUIDE.md) | 公开来源与阅读顺序。 |
| [MIGRATION.md](MIGRATION.md) | 公开迁移来源与范围。 |

原始作品集上下文位于 [AIfile](https://github.com/Daniel-24-life/AIfile)。

## 文档

- [English README](README.en.md)
- [参考指南](docs/reference-guide.md)
- [架构说明](docs/architecture.md)
- [源码阅读指南](docs/SOURCE_READING_GUIDE.md)
- [迁移说明](MIGRATION.md)
- [变更记录](CHANGELOG.md)
