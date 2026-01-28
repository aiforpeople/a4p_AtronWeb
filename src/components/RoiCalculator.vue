<script setup>
import { ref, computed } from 'vue';
import { useI18n } from 'vue-i18n';
import { Calculator } from 'lucide-vue-next';

const { t, locale } = useI18n();

const agentCount = ref(20);
const agentCost = ref(53000);

const annualSavings = computed(() => {
  const savedAgents = agentCount.value * 0.30;
  
  const currencyFormat = locale.value === 'tr' ? 'tr-TR' : 'en-US';
  return (savedAgents * agentCost.value * 12).toLocaleString(currencyFormat, { maximumFractionDigits: 0 });
});
</script>

<template>
  <section class="py-24 bg-white dark:bg-atron-dark transition-colors duration-300">
    <div class="container mx-auto px-4 md:px-6">
        <div class="bg-atron-red rounded-3xl p-8 md:p-16 text-white shadow-2xl overflow-hidden relative">
            <div class="absolute inset-0 opacity-10 pointer-events-none">
                <div class="absolute -right-20 -top-20 w-96 h-96 rounded-full border-4 border-white/30"></div>
                <div class="absolute -left-20 -bottom-20 w-72 h-72 rounded-full border-4 border-white/30"></div>
            </div>

            <div class="relative z-10 grid lg:grid-cols-2 gap-12 items-center">
                <div>
                    <div class="inline-flex items-center gap-2 bg-white/20 px-4 py-1 rounded-full mb-6 backdrop-blur-sm">
                        <Calculator class="w-5 h-5" />
                        <span class="font-bold text-sm">{{ t('roi.title') }}</span>
                    </div>
                    <h2 class="text-3xl md:text-5xl font-black mb-6 leading-tight">
                        {{ t('roi.headline') }}
                    </h2>
                    <p class="text-lg text-white/90 mb-8 max-w-md">
                        {{ t('roi.subtitle') }}
                    </p>
                    <p class="text-xs text-white/60">
                        * {{ t('roi.note') }}
                    </p>
                </div>

                <div class="bg-white dark:bg-slate-800 text-slate-900 dark:text-white p-8 rounded-2xl shadow-xl transition-colors duration-300">
                    
                    <div class="mb-8">
                        <label class="block text-sm font-bold text-slate-500 dark:text-slate-400 mb-2 flex justify-between transition-colors">
                            {{ t('roi.labels.agents') }}
                            <span class="text-atron-red text-lg font-black">{{ agentCount }}</span>
                        </label>
                        <input type="range" v-model="agentCount" min="5" max="500" step="5" 
                               class="w-full h-2 bg-slate-200 dark:bg-slate-700 rounded-lg appearance-none cursor-pointer accent-atron-red transition-colors">
                    </div>

                    <div class="mb-10">
                        <label class="block text-sm font-bold text-slate-500 dark:text-slate-400 mb-2 flex justify-between transition-colors">
                            {{ t('roi.labels.cost') }}
                            <span class="text-slate-900 dark:text-white font-bold">
                                {{ agentCost.toLocaleString(locale === 'tr' ? 'tr-TR' : 'en-US') }} {{ t('roi.currency') }}
                            </span>
                        </label>
                        <input type="range" v-model="agentCost" 
                            :min="locale === 'tr' ? 17002 : 1000" 
                            :max="locale === 'tr' ? 100000 : 5000" 
                            :step="locale === 'tr' ? 1000 : 100" 
                            class="w-full h-2 bg-slate-200 dark:bg-slate-700 rounded-lg appearance-none cursor-pointer accent-slate-900 dark:accent-white transition-colors">
                    </div>

                    <div class="bg-slate-50 dark:bg-slate-900 border border-slate-100 dark:border-slate-700 rounded-xl p-6 text-center transition-colors duration-300">
                        <p class="text-slate-500 dark:text-slate-400 text-sm font-bold uppercase mb-1 transition-colors">{{ t('roi.labels.saved') }}</p>
                        <p class="text-4xl md:text-5xl font-black text-atron-red tracking-tight">
                            {{ t('roi.symbol') }}{{ annualSavings }}
                        </p>
                        <div class="mt-4 inline-block bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400 text-xs font-bold px-3 py-1 rounded-full transition-colors">
                            {{ t('roi.badge') }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </section>
</template>