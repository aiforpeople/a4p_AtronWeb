<script setup>
import { ref } from 'vue';
import { useI18n } from 'vue-i18n';
import { useDark, useToggle } from '@vueuse/core';
import { Sun, Moon, Globe, Menu, X, ChevronDown } from 'lucide-vue-next';
import { availableLocales } from '../i18n';

const { t, locale } = useI18n();
const isDark = useDark();
const toggleDark = useToggle(isDark);
const isMenuOpen = ref(false);
const isLangMenuOpen = ref(false);

const navLinks = ['solution', 'features', 'architecture', 'contact'];

const setLanguage = (lang) => {
  locale.value = lang;
  isLangMenuOpen.value = false;
};
</script>

<template>
  <header class="fixed w-full z-50 bg-white/80 dark:bg-atron-dark/90 backdrop-blur-xl border-b border-white/20 dark:border-gray-800 transition-all duration-300 shadow-sm">
    <div class="container mx-auto px-4 md:px-6 h-24 flex items-center">
      
      <router-link to="/" class="flex items-center gap-2 cursor-pointer transition-transform hover:scale-105 duration-300 flex-shrink-0">
        <img src="/logo.png" alt="ATRON Logo" class="h-10 md:h-12 w-auto object-contain" />
      </router-link>

      <nav class="hidden md:flex items-center gap-6 ml-8">
        <router-link 
          v-for="key in navLinks" 
          :key="key" 
          :to="{ name: 'home', hash: `#${key}` }" 
          class="text-sm font-bold text-slate-600 dark:text-slate-300 hover:text-atron-red dark:hover:text-white transition-colors relative group py-2"
          active-class=""
          exact-active-class=""
        >
          {{ t(`nav.${key}`) }}
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-atron-red transition-all duration-300 group-hover:w-full"></span>
        </router-link>
      </nav>

      <div class="hidden md:flex items-center gap-3 ml-auto">
        
        <div class="flex items-center gap-2 bg-slate-50 dark:bg-slate-800/50 rounded-full p-1 border border-slate-200 dark:border-slate-700">
            
            <div class="relative">
              <button @click="isLangMenuOpen = !isLangMenuOpen" class="flex items-center gap-1.5 px-3 py-2 rounded-full hover:bg-white dark:hover:bg-slate-700 transition-all text-xs font-bold uppercase cursor-pointer text-slate-700 dark:text-slate-200">
                <Globe class="w-3.5 h-3.5" />
                <span>{{ locale }}</span>
                <ChevronDown class="w-3 h-3 opacity-50" />
              </button>
              
              <div v-if="isLangMenuOpen" class="absolute right-0 top-full mt-3 p-2 align-center bg-white dark:bg-atron-surface border border-gray-100 dark:border-gray-700 rounded-2xl shadow-2xl overflow-hidden py-2 transform origin-top-right transition-all z-50">
                <button v-for="lang in availableLocales" :key="lang" @click="setLanguage(lang)"
                        class="w-full text-left px-4 py-2.5 text-sm hover:bg-slate-50 dark:hover:bg-slate-700 uppercase cursor-pointer flex items-center gap-2 transition-colors"
                        :class="{ 'text-atron-red font-bold bg-red-50 dark:bg-red-900/10': locale === lang, 'text-slate-600 dark:text-slate-300': locale !== lang }">
                  {{ lang }}
                </button>
              </div>
            </div>

            <div class="w-px h-4 bg-slate-300 dark:bg-slate-600 mx-1"></div>

            <button @click="toggleDark()" class="p-2 rounded-full hover:bg-white dark:hover:bg-slate-700 transition text-slate-600 dark:text-yellow-400 cursor-pointer hover:shadow-sm">
              <Sun v-if="isDark" class="w-4 h-4" />
              <Moon v-else class="w-4 h-4" />
            </button>
        </div>

        <a href="#contact" class="ml-2 bg-atron-red text-white px-6 py-3 rounded-full font-bold text-sm hover:bg-red-700 transition-all shadow-lg shadow-red-500/30 hover:shadow-red-500/50 hover:-translate-y-0.5 active:translate-y-0">
          {{ t('hero.cta') }}
        </a>
      </div>

      <button @click="isMenuOpen = !isMenuOpen" class="md:hidden ml-auto p-2 text-slate-600 dark:text-slate-200 cursor-pointer bg-slate-100 dark:bg-slate-800 rounded-lg hover:bg-slate-200 transition-colors">
        <Menu v-if="!isMenuOpen" class="w-6 h-6" />
        <X v-else class="w-6 h-6" />
      </button>
    </div>

    <transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <div v-if="isMenuOpen" class="md:hidden bg-white/95 dark:bg-atron-surface/95 backdrop-blur-xl border-b dark:border-gray-700 shadow-2xl absolute w-full left-0 top-24 pb-6 px-4 flex flex-col gap-2">
        <a v-for="key in navLinks" :key="key" :href="`#${key}`" @click="isMenuOpen = false"
           class="text-lg font-semibold text-slate-600 dark:text-slate-300 py-3 px-4 rounded-xl hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors">
          {{ t(`nav.${key}`) }}
        </a>
        
        <div class="h-px bg-slate-100 dark:bg-slate-700 my-2"></div>
        
        <div class="flex items-center justify-between px-4 py-2">
           <div class="flex gap-2">
              <button v-for="lang in availableLocales" :key="lang" @click="setLanguage(lang)" 
                class="px-4 py-2 rounded-lg bg-slate-100 dark:bg-slate-800 text-xs font-bold uppercase transition-all"
                :class="{ 'ring-2 ring-atron-red text-atron-red bg-red-50 dark:bg-red-900/20': locale === lang }">
                {{ lang }}
              </button>
           </div>
           <button @click="toggleDark()" class="p-3 bg-slate-100 dark:bg-slate-800 rounded-lg">
              <Sun v-if="isDark" class="w-5 h-5 text-yellow-400" />
              <Moon v-else class="w-5 h-5 text-slate-600" />
           </button>
        </div>
      </div>
    </transition>
  </header>
</template>