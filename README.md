# 园林绿化养护平台

面向城市绿地、行道树、花坛花境、灌溉设施与病虫害防治的养护计划、巡查整改与验收的一体化养护后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 公共绿地 | `greenland` | 公共绿地 | 绿地编码、绿地名称、绿地类型 |
| 行道树 | `streettree` | 行道树 | 树木编号、树种名称、胸径 |
| 花坛花境 | `flowerbed` | 花坛花境 | 花坛编号、所在绿地、花卉品种 |
| 苗木繁育 | `nursery` | 苗圃苗木 | 苗圃编号、苗木品种、规格等级 |
| 灌溉设施 | `irrigation` | 灌溉设施 | 设施编号、设施类型、所在绿地 |
| 修剪整形 | `pruning` | 修剪单 | 修剪单号、修剪对象、修剪方式 |
| 病虫害防治 | `pest` | 防治单 | 防治单号、有害生物、危害对象 |
| 施肥养护 | `fertilize` | 施肥单 | 施肥单号、施肥对象、肥料品种 |
| 补植更新 | `replant` | 补植单 | 补植单号、补植位置、补植品种 |
| 古树名木 | `ancient` | 古树名木 | 古树编号、树种名称、树龄 |
| 巡查检查 | `patrol` | 巡查单 | 巡查单号、巡查路线、巡查人员 |
| 整改处置 | `rectify` | 整改单 | 整改单号、关联问题、整改措施 |
| 园林设施 | `facility` | 园林设施 | 设施编号、设施类型、所在绿地 |
| 养护验收 | `accept` | 养护验收单 | 验收单号、关联任务、验收项目 |
| 养护计划 | `plan` | 养护计划 | 计划编号、养护类型、养护对象 |
| 时令布置 | `season` | 时令布置单 | 布置单号、布置节点、布置位置 |
| 水体养护 | `waterbody` | 景观水体 | 水体编号、水体类型、所在绿地 |
| 养护记录 | `record` | 养护记录 | 记录编号、养护对象、作业类型 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
