<script setup>
import AppHeader from '../components/AppHeader.vue';
import AppFooter from '../components/AppFooter.vue';
</script>

<template>
  <div class="min-h-screen flex flex-col font-sans bg-atron-light text-slate-800 dark:bg-atron-dark dark:text-slate-100 transition-colors duration-300">
    <AppHeader />

    <main class="flex-grow pt-20">
      <slot />
    </main>

    <AppFooter />
  </div>
</template>