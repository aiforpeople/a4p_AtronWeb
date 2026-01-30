<script setup>
import { useI18n } from 'vue-i18n';
const { t } = useI18n();
</script>

<template>
  <section id="solution" class="relative overflow-hidden min-h-[90vh] flex items-center">
    
    <div class="absolute inset-0 z-0">
        <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
        <div class="absolute left-0 right-0 top-0 -z-10 m-auto h-[310px] w-[310px] rounded-full bg-atron-red opacity-20 blur-[100px]"></div>
    </div>

    <div class="container mx-auto px-4 md:px-6 relative z-10 grid md:grid-cols-2 gap-12 items-center">
        
        <div class="text-left space-y-6">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-100 dark:bg-red-900/30 text-atron-red text-xs font-bold uppercase tracking-wider">
                <span class="relative flex h-2 w-2">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
                  <span class="relative inline-flex rounded-full h-2 w-2 bg-red-500"></span>
                </span>
                AI-Native CRM & Call Center
            </div>

            <h1 class="text-5xl md:text-7xl font-black leading-tight tracking-tight text-slate-900 dark:text-white">
                {{ t('hero.title').split('AI-Native')[0] }}
                <span class="text-atron-red">AI-Native</span>
                {{ t('hero.title').split('AI-Native')[1] }}
            </h1>
            
            <p class="text-lg md:text-xl text-slate-600 dark:text-slate-300 leading-relaxed max-w-lg">
                {{ t('hero.subtitle') }}
            </p>

            <div class="flex flex-col sm:flex-row gap-4 pt-4">
                <router-link 
                :to="{ name: 'home', hash: '#contact' }" 
                class="inline-flex items-center justify-center px-8 py-4 text-base font-bold text-white transition-all duration-200 bg-atron-red rounded-xl hover:bg-red-700 hover:shadow-lg hover:shadow-red-500/30 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                >
                    {{ t('hero.cta') }}
                </router-link>
            </div>

            <div class="pt-8 border-t border-slate-200 dark:border-slate-800 grid grid-cols-3 gap-4 text-center md:text-left">
                <div>
                    <p class="text-2xl font-black text-slate-900 dark:text-white">7/24</p>
                    <p class="text-xs text-slate-500 uppercase">{{ t('hero.stats.ai') }}</p>
                </div>
                <div>
                    <p class="text-2xl font-black text-slate-900 dark:text-white">%40</p>
                    <p class="text-xs text-slate-500 uppercase">{{ t('hero.stats.cost') }}</p>
                </div>
                <div>
                    <p class="text-2xl font-black text-slate-900 dark:text-white">100+</p>
                    <p class="text-xs text-slate-500 uppercase">{{ t('hero.stats.lang') }}</p>
                </div>
            </div>
        </div>

        <div class="relative hidden md:block">
                <img src="@/assets/hero.png" 
                     alt="Dashboard" 
                     class="rounded-xl w-full h-auto " />
        </div>
    </div>
  </section>
</template>