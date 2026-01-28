<script setup>
import { computed } from 'vue';
import { useI18n } from 'vue-i18n';
import { useRouter } from 'vue-router';
import { Scale, ArrowLeft } from 'lucide-vue-next';

const { t, tm } = useI18n();
const router = useRouter();

const sections = computed(() => {
  const items = tm('legal.terms.sections');
  return Array.isArray(items) ? items : [];
});
</script>

<template>
  <div class="pt-32 pb-20 bg-slate-50 dark:bg-slate-900 min-h-screen transition-colors duration-300">
    <div class="container mx-auto px-4 md:px-6 max-w-6xl">
      
      <button @click="router.push('/')" class="mb-8 flex items-center gap-2 text-slate-500 hover:text-atron-red transition-colors text-sm font-bold uppercase tracking-wide cursor-pointer group">
        <ArrowLeft class="w-4 h-4 transition-transform group-hover:-translate-x-1" />
        {{ t('nav.back_home') || 'Ana Sayfaya Dön' }}
      </button>

      <div class="bg-white dark:bg-atron-surface p-8 md:p-12 rounded-3xl shadow-xl border border-slate-100 dark:border-slate-700">
        
        <div class="flex items-center gap-4 mb-8 pb-8 border-b border-slate-100 dark:border-slate-700">
          <div class="w-12 h-12 rounded-2xl bg-blue-50 dark:bg-blue-900/20 text-blue-600 flex items-center justify-center shrink-0">
            <Scale class="w-6 h-6" />
          </div>
          <div>
            <h1 class="text-3xl md:text-4xl font-black text-slate-900 dark:text-white">
              {{ t('legal.terms.title') }}
            </h1>
            <p class="text-slate-500 dark:text-slate-400 mt-1 text-sm">
              {{ t('legal.terms.date') }}
            </p>
          </div>
        </div>

        <div class="space-y-8 text-slate-600 dark:text-slate-300 leading-relaxed">
          <div v-for="(section, index) in sections" :key="index">
            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3">
              {{ section.title }}
            </h3>
            <p class="whitespace-pre-line">
              {{ section.content }}
            </p>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>