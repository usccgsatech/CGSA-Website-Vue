<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'

// Navigation item interfaces
interface DropdownItem {
  text: string
  href: string
}

interface NavItem {
  text: string
  href: string
  isActive?: boolean
  dropdown?: DropdownItem[]
}

// Navigation data
const navItems: NavItem[] = [
  {
    text: '主页',
    href: '/',
  },
  {
    text: '关于我们',
    href: '#',
    dropdown: [
      { text: '组织介绍', href: '/about/cgsa-intro' },
      { text: '主席团成员', href: '/about/board-members' },
      { text: '部门介绍', href: '/about/departments' }
    ]
  },
  {
    text: 'CGSA 校园',
    href: '#',
    dropdown: [
      { text: '新生福利', href: '/welfare' },
      { text: 'CGSA 职业', href: '/career' },
      { text: 'CGSA 活动', href: '/activity' }
    ]
  },
  {
    text: 'CGSA 校友',
    href: '/alumni'
  },
  {
    text: '联系我们',
    href: '/contact'
  }
]
</script>

<template>
  <div id="app">
    <!-- Stylized Banner/Header -->
    <header class="app-header">
      <div class="header-content">
        <div class="logo-section">
          <h1 class="logo">CGSA</h1>
          <p class="tagline">USC Chinese Graduate Student Association</p>
        </div>

        <!-- Navigation Bar -->
        <nav class="navbar navbar-expand-md navbar-light bg-light">
          <div class="container-fluid">
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
              data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
              aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li v-for="(item, index) in navItems" :key="index" class="nav-item"
                  :class="{ 'dropdown': item.dropdown }">
                  <!-- Regular nav link -->
                  <a v-if="!item.dropdown" class="nav-link" :href="item.href">
                    {{ item.text }}
                  </a>

                  <!-- Dropdown nav link -->
                  <template v-else>
                    <a class="nav-link dropdown-toggle" :href="item.href" :id="`navbarDropdown${index}`" role="button"
                      data-bs-toggle="dropdown" aria-expanded="false">
                      {{ item.text }}
                    </a>
                    <ul class="dropdown-menu" :aria-labelledby="`navbarDropdown${index}`">
                      <li v-for="(dropdownItem, dropdownIndex) in item.dropdown" :key="dropdownIndex">
                        <a class="dropdown-item" :href="dropdownItem.href">
                          {{ dropdownItem.text }}
                        </a>
                      </li>
                    </ul>
                  </template>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <RouterView />
    </main>

    <!-- Footer -->
    <footer class="app-footer">
      <div class="footer-content">
        <p>&copy; 2024 USC Chinese Graduate Student Association. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.navigation {
  display: flex;
  gap: 1rem;
  align-items: center;
}


.app-footer {
  background: #151b24;
  color: white;
  padding: 1rem 0;
  margin-top: auto;
}

.footer-content {
  margin: 0 auto;
  padding: 0 2rem;
}

.footer-links {
  display: flex;
  gap: 2rem;
}
</style>
