<script setup>
import { ref } from 'vue';
import { useI18n } from 'vue-i18n';
import { Headset, TrendingUp, ShieldCheck, CheckCircle2, XCircle } from 'lucide-vue-next';

const { t, tm } = useI18n();
const activeTab = ref('ops');

const getList = (path) => {
  const items = tm(path);
  return Array.isArray(items) ? items : [];
};
</script>

<template>
  <section id="features" class="py-24 bg-white dark:bg-atron-dark transition-colors">
    <div class="container mx-auto px-4 md:px-6">
      <div class="text-center mb-16">
        <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-4">
          {{ t('solutions.title') }}
        </h2>
        <p class="text-slate-600 dark:text-slate-400 text-lg max-w-2xl mx-auto">
          {{ t('solutions.subtitle') }}
        </p>
      </div>

      <div class="flex flex-wrap justify-center gap-4 mb-12">
        <button @click="activeTab = 'ops'" :class="['flex items-center gap-2 px-6 py-3 rounded-full font-bold transition-all border cursor-pointer', activeTab === 'ops' ? 'bg-atron-red text-white border-atron-red shadow-lg' : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700 hover:border-atron-red']">
          <Headset class="w-5 h-5" /> {{ t('solutions.tabs.ops') }}
        </button>
        <button @click="activeTab = 'sales'" :class="['flex items-center gap-2 px-6 py-3 rounded-full font-bold transition-all border cursor-pointer', activeTab === 'sales' ? 'bg-atron-red text-white border-atron-red shadow-lg' : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700 hover:border-atron-red']">
          <TrendingUp class="w-5 h-5" /> {{ t('solutions.tabs.sales') }}
        </button>
        <button @click="activeTab = 'it'" :class="['flex items-center gap-2 px-6 py-3 rounded-full font-bold transition-all border cursor-pointer', activeTab === 'it' ? 'bg-atron-red text-white border-atron-red shadow-lg' : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700 hover:border-atron-red']">
          <ShieldCheck class="w-5 h-5" /> {{ t('solutions.tabs.it') }}
        </button>
      </div>

      <div class="bg-slate-50 dark:bg-atron-surface rounded-3xl p-8 md:p-12 border border-slate-100 dark:border-slate-700 shadow-2xl min-h-[400px]">
        <transition mode="out-in" enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 translate-y-2" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 -translate-y-2">
          
          <div :key="activeTab" class="grid md:grid-cols-2 gap-12 items-center">
            <div>
              <div class="inline-block px-3 py-1 rounded-md bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300 text-xs font-bold uppercase tracking-wider mb-4">
                {{ t(`solutions.${activeTab}.role`) }}
              </div>
              <h3 class="text-3xl font-bold text-slate-900 dark:text-white mb-8">
                {{ t(`solutions.${activeTab}.title`) }}
              </h3>

              <div class="space-y-8">
                <div class="relative pl-6 border-l-4 border-gray-300 dark:border-gray-600">
                  <h4 class="text-lg font-bold text-gray-500 dark:text-gray-400 mb-3 flex items-center gap-2">
                    <XCircle class="w-5 h-5" /> {{ t(`solutions.${activeTab}.before.title`) }}
                  </h4>
                  <ul class="space-y-2">
                    <li v-for="(item, index) in getList(`solutions.${activeTab}.before.list`)" :key="index" class="text-gray-500 text-sm md:text-base">
                      • {{ item }}
                    </li>
                  </ul>
                </div>

                <div class="relative pl-6 border-l-4 border-atron-red bg-red-50/50 dark:bg-red-900/10 py-2 pr-2 rounded-r-lg">
                  <h4 class="text-lg font-bold text-atron-red mb-3 flex items-center gap-2">
                    <CheckCircle2 class="w-5 h-5" /> {{ t(`solutions.${activeTab}.after.title`) }}
                  </h4>
                  <ul class="space-y-2">
                    <li v-for="(item, index) in getList(`solutions.${activeTab}.after.list`)" :key="index" class="text-slate-800 dark:text-slate-200 font-medium text-sm md:text-base flex items-start gap-2">
                      <span class="text-green-500 mt-1">✓</span> {{ item }}
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <div class="relative h-full min-h-[300px] rounded-2xl overflow-hidden shadow-lg">
                <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent z-10"></div>
                <img v-if="activeTab === 'ops'" src="https://images.unsplash.com/photo-1556745753-b2904692b3cd?auto=format&fit=crop&w=800&q=80" class="absolute inset-0 w-full h-full object-cover" />
                <img v-if="activeTab === 'sales'" src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80" class="absolute inset-0 w-full h-full object-cover" />
                <img v-if="activeTab === 'it'" src="https://images.unsplash.com/photo-1558494949-ef2a2cc58fa9?auto=format&fit=crop&w=800&q=80" class="absolute inset-0 w-full h-full object-cover" />
            </div>

          </div>
        </transition>
      </div>
    </div>
  </section>
</template>