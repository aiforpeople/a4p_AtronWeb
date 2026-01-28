<script setup>
import { useI18n } from 'vue-i18n';
const { t } = useI18n();
</script>

<template>
  <section class="py-24 bg-slate-50 dark:bg-slate-900/50 transition-colors">
    <div class="container mx-auto px-4 md:px-6">
        <div class="grid md:grid-cols-3 gap-8">
            <div class="group bg-white dark:bg-atron-surface p-8 rounded-2xl shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border border-slate-100 dark:border-slate-700">
                <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">{{ t('pain.cards.aht.title') }}</h3>
                <div class="text-4xl font-black text-slate-900 dark:text-white mb-4 tracking-tight">
                    {{ t('pain.cards.aht.stat') }}
                    <span class="text-base font-normal text-slate-500 block mt-1">{{ t('pain.cards.aht.suffix') }}</span>
                </div>
                <p class="text-slate-600 dark:text-slate-400 leading-relaxed">{{ t('pain.cards.aht.desc') }}</p>
            </div>

            <div class="group bg-white dark:bg-atron-surface p-8 rounded-2xl shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border border-slate-100 dark:border-slate-700">
                <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">{{ t('pain.cards.churn.title') }}</h3>
                <div class="text-4xl font-black text-slate-900 dark:text-white mb-4 tracking-tight">
                    {{ t('pain.cards.churn.stat') }}
                    <span class="text-base font-normal text-slate-500 block mt-1">{{ t('pain.cards.churn.suffix') }}</span>
                </div>
                <p class="text-slate-600 dark:text-slate-400 leading-relaxed">{{ t('pain.cards.churn.desc') }}</p>
            </div>

            <div class="group bg-white dark:bg-atron-surface p-8 rounded-2xl shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border border-slate-100 dark:border-slate-700">
                <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">{{ t('pain.cards.quality.title') }}</h3>
                <div class="text-4xl font-black text-slate-900 dark:text-white mb-4 tracking-tight">
                    {{ t('pain.cards.quality.stat') }}
                    <span class="text-base font-normal text-slate-500 block mt-1">{{ t('pain.cards.quality.suffix') }}</span>
                </div>
                <p class="text-slate-600 dark:text-slate-400 leading-relaxed">{{ t('pain.cards.quality.desc') }}</p>
            </div>
        </div>

        <div class="mt-16 text-center">
            <p class="text-lg font-medium text-slate-900 dark:text-white">
                {{ t('pain.footer.text') }}
                <span class="text-slate-500 dark:text-slate-400">
                    {{ t('pain.footer.highlight') }}
                </span>
            </p>
        </div>
    </div>
  </section>
</template>