<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">园林绿化养护平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向城市绿地、行道树、花坛花境、灌溉设施与病虫害防治的养护计划、巡查整改与验收的一体化养护后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "公共绿地", path: "/greenland" }, { label: "行道树", path: "/streettree" }, { label: "花坛花境", path: "/flowerbed" }, { label: "苗木繁育", path: "/nursery" }, { label: "灌溉设施", path: "/irrigation" }, { label: "修剪整形", path: "/pruning" }, { label: "病虫害防治", path: "/pest" }, { label: "施肥养护", path: "/fertilize" }, { label: "补植更新", path: "/replant" }, { label: "古树名木", path: "/ancient" }, { label: "巡查检查", path: "/patrol" }, { label: "整改处置", path: "/rectify" }, { label: "园林设施", path: "/facility" }, { label: "养护验收", path: "/accept" }, { label: "养护计划", path: "/plan" }, { label: "时令布置", path: "/season" }, { label: "水体养护", path: "/waterbody" }, { label: "养护记录", path: "/record" }]
</script>
