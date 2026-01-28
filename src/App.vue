<script setup>
import { ref, computed } from 'vue';
import { useI18n } from 'vue-i18n';
import { useDark, useToggle } from '@vueuse/core';
import { 
  Sun, Moon, Globe, Menu, X, Clock, Users, AlertTriangle, ArrowRight,
  Headset, TrendingUp, ShieldCheck, CheckCircle2, XCircle,
  PhoneIncoming, Mic, BrainCircuit, DatabaseZap, Layers, Server,
  Calculator, Mail, Linkedin, Twitter
} from 'lucide-vue-next';

const { t, locale, tm } = useI18n();

const isDark = useDark();
const toggleDark = useToggle(isDark);

const isMenuOpen = ref(false);
const activeTab = ref('ops');
const agentCount = ref(20);
const agentCost = ref(53000);

const toggleLanguage = () => {
  locale.value = locale.value === 'tr' ? 'en' : 'tr';
};

const navLinks = [
  { key: 'solution', href: '#solution' },
  { key: 'features', href: '#features' },
  { key: 'architecture', href: '#architecture' },
  { key: 'contact', href: '#contact' },
];

const annualSavings = computed(() => {
  const savedAgents = agentCount.value * 0.30;
  return (savedAgents * agentCost.value * 12).toLocaleString('tr-TR', { maximumFractionDigits: 0 });
});
</script>

<template>
  <div class="min-h-screen flex flex-col font-sans">

    <header class="fixed w-full z-50 bg-white/80 dark:bg-atron-dark/90 backdrop-blur-md border-b border-gray-200 dark:border-gray-800 transition-colors duration-300">
      <div class="container mx-auto px-4 md:px-6 h-20 flex items-center justify-between">

        <div class="flex items-center gap-2">
          <span class="text-3xl font-black tracking-tighter text-atron-red">ATRON</span>
        </div>

        <nav class="hidden md:flex items-center gap-8">
          <a v-for="link in navLinks" :key="link.key" :href="link.href" class="text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-atron-red dark:hover:text-atron-red transition-colors">
            {{ t(`nav.${link.key}`) }}
          </a>
        </nav>

        <div class="hidden md:flex items-center gap-4">
          <button @click="toggleLanguage" class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-slate-800 transition cursor-pointer">
            <span class="font-bold text-xs">{{ locale.toUpperCase() }}</span>
          </button>

          <button @click="toggleDark()" class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-slate-800 transition cursor-pointer">
            <Sun v-if="isDark" class="w-5 h-5 text-yellow-400" />
            <Moon v-else class="w-5 h-5 text-slate-600" />
          </button>

          <a href="#contact" class="bg-atron-red text-white px-5 py-2.5 rounded-lg font-bold text-sm hover:bg-red-700 transition shadow-lg shadow-red-500/30">
            {{ t('hero.cta') }}
          </a>
        </div>

        <button @click="isMenuOpen = !isMenuOpen" class="md:hidden p-2 text-slate-600 dark:text-slate-200 cursor-pointer">
          <Menu v-if="!isMenuOpen" class="w-6 h-6" />
          <X v-else class="w-6 h-6" />
        </button>
      </div>

      <div v-if="isMenuOpen" class="md:hidden bg-white dark:bg-atron-surface border-t dark:border-gray-700 p-4 flex flex-col gap-4 shadow-xl">
        <a v-for="link in navLinks" :key="link.key" :href="link.href" @click="isMenuOpen = false" class="text-base font-medium text-slate-600 dark:text-slate-300 py-2 border-b border-gray-100 dark:border-gray-700">
          {{ t(`nav.${link.key}`) }}
        </a>
        <div class="flex items-center justify-between pt-2">
          <button @click="toggleLanguage" class="flex items-center gap-2 text-sm font-bold">
            <Globe class="w-4 h-4" /> {{ locale === 'tr' ? 'English' : 'Türkçe' }}
          </button>
          <button @click="toggleDark()" class="p-2">
            <Sun v-if="isDark" class="w-5 h-5 text-yellow-400" />
            <Moon v-else class="w-5 h-5 text-slate-600" />
          </button>
        </div>
      </div>
    </header>

    <main class="flex-grow pt-20">

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
              <a href="#contact" class="inline-flex items-center justify-center px-8 py-4 text-base font-bold text-white transition-all duration-200 bg-atron-red rounded-xl hover:bg-red-700 hover:shadow-lg hover:shadow-red-500/30 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
                {{ t('hero.cta') }}
              </a>
              <button class="inline-flex items-center justify-center px-8 py-4 text-base font-bold text-slate-700 dark:text-white transition-all duration-200 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl hover:bg-slate-50 dark:hover:bg-slate-700 focus:outline-none">
                Showreel izle
              </button>
            </div>

            <div class="pt-8 border-t border-slate-200 dark:border-slate-800 grid grid-cols-3 gap-4 text-center md:text-left">
              <div>
                <p class="text-2xl font-black text-slate-900 dark:text-white">7/24</p>
                <p class="text-xs text-slate-500 uppercase">AI Operasyon</p>
              </div>
              <div>
                <p class="text-2xl font-black text-slate-900 dark:text-white">%40</p>
                <p class="text-xs text-slate-500 uppercase">Maliyet Düşüşü</p>
              </div>
              <div>
                <p class="text-2xl font-black text-slate-900 dark:text-white">100+</p>
                <p class="text-xs text-slate-500 uppercase">Dil Desteği</p>
              </div>
            </div>
          </div>

          <div class="relative hidden md:block">
            <div class="relative bg-gradient-to-br from-slate-100 to-white dark:from-slate-800 dark:to-slate-900 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-2xl p-2 rotate-2 hover:rotate-0 transition-transform duration-500">
              <div class="absolute -top-4 -right-4 bg-white dark:bg-atron-surface p-4 rounded-lg shadow-xl border border-slate-100 dark:border-slate-700 animate-bounce">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full bg-green-100 flex items-center justify-center text-green-600">
                    📞
                  </div>
                  <div>
                    <p class="text-xs font-bold text-slate-500">Gelen Çağrı</p>
                    <p class="text-sm font-bold text-slate-900 dark:text-white">Müşteri Talebi</p>
                  </div>
                </div>
              </div>

              <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" alt="Dashboard" class="rounded-xl w-full h-auto object-cover opacity-90 grayscale hover:grayscale-0 transition-all duration-500" />
            </div>
          </div>

        </div>
      </section>

      <section class="py-24 bg-slate-50 dark:bg-slate-900/50 transition-colors">
        <div class="container mx-auto px-4 md:px-6">

          <div class="text-center max-w-3xl mx-auto mb-16">
            <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-4">
              {{ t('pain.title') }}
            </h2>
            <p class="text-slate-600 dark:text-slate-400 text-lg">
              {{ t('pain.subtitle') }}
            </p>
          </div>

          <div class="grid md:grid-cols-3 gap-8">

            <div class="group bg-white dark:bg-atron-surface p-8 rounded-2xl shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border border-slate-100 dark:border-slate-700">
              <div class="w-14 h-14 bg-red-50 dark:bg-red-900/20 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                <Clock class="w-7 h-7 text-atron-red" />
              </div>
              <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">{{ t('pain.cards.aht.title') }}</h3>
              <div class="text-4xl font-black text-slate-900 dark:text-white mb-4 tracking-tight">
                {{ t('pain.cards.aht.stat') }}
                <span class="text-base font-normal text-slate-500 block mt-1">/ {{ locale === 'tr' ? 'yıl' : 'year' }}</span>
              </div>
              <p class="text-slate-600 dark:text-slate-400 leading-relaxed">
                {{ t('pain.cards.aht.desc') }}
              </p>
            </div>

            <div class="group bg-white dark:bg-atron-surface p-8 rounded-2xl shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border border-slate-100 dark:border-slate-700">
              <div class="w-14 h-14 bg-orange-50 dark:bg-orange-900/20 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                <Users class="w-7 h-7 text-orange-600" />
              </div>
              <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">{{ t('pain.cards.churn.title') }}</h3>
              <div class="text-4xl font-black text-slate-900 dark:text-white mb-4 tracking-tight">
                {{ t('pain.cards.churn.stat') }}
                <span class="text-base font-normal text-slate-500 block mt-1">{{ locale === 'tr' ? 'Devir Oranı' : 'Turnover' }}</span>
              </div>
              <p class="text-slate-600 dark:text-slate-400 leading-relaxed">
                {{ t('pain.cards.churn.desc') }}
              </p>
            </div>

            <div class="group bg-white dark:bg-atron-surface p-8 rounded-2xl shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border border-slate-100 dark:border-slate-700">
              <div class="w-14 h-14 bg-blue-50 dark:bg-blue-900/20 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                <AlertTriangle class="w-7 h-7 text-blue-600" />
              </div>
              <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">{{ t('pain.cards.quality.title') }}</h3>
              <div class="text-4xl font-black text-slate-900 dark:text-white mb-4 tracking-tight">
                {{ t('pain.cards.quality.stat') }}
                <span class="text-base font-normal text-slate-500 block mt-1">{{ locale === 'tr' ? 'Veri Kaybı' : 'Data Loss' }}</span>
              </div>
              <p class="text-slate-600 dark:text-slate-400 leading-relaxed">
                {{ t('pain.cards.quality.desc') }}
              </p>
            </div>

          </div>

          <div class="mt-16 text-center">
            <p class="text-lg font-medium text-slate-900 dark:text-white">
              {{ locale === 'tr' ? 'Rekabet her geçen gün artıyor.' : 'Competition is rising every day.' }}
              <span class="text-slate-500 dark:text-slate-400">
                {{ locale === 'tr' ? 'Eski modelde ısrar etmek büyümenizi engelliyor.' : 'Staying in the old model is capping your growth.' }}
              </span>
            </p>
          </div>

        </div>
      </section>

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
            <button @click="activeTab = 'ops'" :class="['flex items-center gap-2 px-6 py-3 rounded-full font-bold transition-all duration-300 border',
              activeTab === 'ops' ? 'bg-atron-red text-white border-atron-red shadow-lg shadow-red-500/30' : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700 hover:border-atron-red']">
              <Headset class="w-5 h-5" />
              {{ t('solutions.tabs.ops') }}
            </button>

            <button @click="activeTab = 'sales'" :class="['flex items-center gap-2 px-6 py-3 rounded-full font-bold transition-all duration-300 border',
              activeTab === 'sales' ? 'bg-atron-red text-white border-atron-red shadow-lg shadow-red-500/30' : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700 hover:border-atron-red']">
              <TrendingUp class="w-5 h-5" />
              {{ t('solutions.tabs.sales') }}
            </button>

            <button @click="activeTab = 'it'" :class="['flex items-center gap-2 px-6 py-3 rounded-full font-bold transition-all duration-300 border',
              activeTab === 'it' ? 'bg-atron-red text-white border-atron-red shadow-lg shadow-red-500/30' : 'bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700 hover:border-atron-red']">
              <ShieldCheck class="w-5 h-5" />
              {{ t('solutions.tabs.it') }}
            </button>
          </div>

          <div class="bg-slate-50 dark:bg-atron-surface rounded-3xl p-8 md:p-12 border border-slate-100 dark:border-slate-700 shadow-2xl transition-all duration-500 min-h-[400px]">

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
                        <li v-for="(item, index) in tm(`solutions.${activeTab}.after.list`)" :key="index" class="text-slate-800 dark:text-slate-200 font-medium text-sm md:text-base flex items-start gap-2">
                          <span class="text-green-500 mt-1">✓</span> {{ item }}
                        </li>
                      </ul>
                    </div>

                    <div class="relative pl-6 border-l-4 border-atron-red bg-red-50/50 dark:bg-red-900/10 py-2 -ml-2 pr-2 rounded-r-lg">
                      <h4 class="text-lg font-bold text-atron-red mb-3 flex items-center gap-2">
                        <CheckCircle2 class="w-5 h-5" /> {{ t(`solutions.${activeTab}.after.title`) }}
                      </h4>
                      <ul class="space-y-2">
                        <li v-for="(item, index) in tm(`solutions.${activeTab}.after.list`)" :key="index" class="text-slate-800 dark:text-slate-200 font-medium text-sm md:text-base flex items-start gap-2">
                          <span class="text-green-500 mt-1">✓</span> {{ item }}
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>

                <div class="relative h-full min-h-[300px] rounded-2xl overflow-hidden shadow-lg group">
                  <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent z-10"></div>

                  <img v-if="activeTab === 'ops'" src="https://images.unsplash.com/photo-1556745753-b2904692b3cd?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" class="absolute inset-0 w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" alt="Operations" />
                  <img v-if="activeTab === 'sales'" src="https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" class="absolute inset-0 w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" alt="Sales" />
                  <img v-if="activeTab === 'it'" src="https://images.unsplash.com/photo-1558494949-ef2a2cc58fa9?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" class="absolute inset-0 w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" alt="IT" />

                  <div class="absolute bottom-6 left-6 z-20">
                    <span class="bg-atron-red text-white text-xs font-bold px-3 py-1 rounded-full mb-2 inline-block">ATRON AI</span>
                    <p class="text-white font-medium text-sm opacity-90">
                      {{ activeTab === 'ops' ? 'Gerçek zamanlı izleme' : (activeTab === 'sales' ? 'Otomatik CRM Güncellemesi' : 'Güvenli API Entegrasyonu') }}
                    </p>
                  </div>
                </div>

              </div>
            </transition>
          </div>

        </div>
      </section>

      <section id="architecture" class="py-24 bg-slate-50 dark:bg-slate-900/50 relative overflow-hidden">
        
        <div class="absolute top-0 right-0 w-1/3 h-full bg-gradient-to-l from-slate-200/50 dark:from-slate-800/50 to-transparent pointer-events-none"></div>

        <div class="container mx-auto px-4 md:px-6 relative z-10">
            
            <div class="mb-16">
                <h2 class="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-4">
                    {{ t('tech.title') }}
                </h2>
                <p class="text-slate-600 dark:text-slate-400 text-lg">
                    {{ t('tech.subtitle') }}
                </p>
            </div>

            <div class="grid lg:grid-cols-2 gap-16 items-start">
                
                <div>
                    <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-8 flex items-center gap-2">
                        <ArrowRight class="text-atron-red" /> {{ t('tech.journey.title') }}
                    </h3>
                    
                    <div class="relative pl-8 border-l-2 border-slate-200 dark:border-slate-700 space-y-12">
                        <div class="relative">
                            <div class="absolute -left-[41px] top-0 w-10 h-10 bg-white dark:bg-atron-surface border-2 border-atron-red rounded-full flex items-center justify-center text-atron-red shadow-lg">
                                <PhoneIncoming class="w-5 h-5" />
                            </div>
                            <h4 class="text-xl font-bold text-slate-900 dark:text-white mb-2">{{ tm('tech.journey.steps')[0].title }}</h4>
                            <p class="text-slate-600 dark:text-slate-400">{{ tm('tech.journey.steps')[0].desc }}</p>
                        </div>
                        
                        <div class="relative">
                            <div class="absolute -left-[41px] top-0 w-10 h-10 bg-white dark:bg-atron-surface border-2 border-slate-300 dark:border-slate-600 rounded-full flex items-center justify-center text-slate-500 shadow-sm">
                                <Mic class="w-5 h-5" />
                            </div>
                            <h4 class="text-xl font-bold text-slate-900 dark:text-white mb-2">{{ tm('tech.journey.steps')[1].title }}</h4>
                            <p class="text-slate-600 dark:text-slate-400">{{ tm('tech.journey.steps')[1].desc }}</p>
                        </div>

                        <div class="relative">
                            <div class="absolute -left-[41px] top-0 w-10 h-10 bg-white dark:bg-atron-surface border-2 border-slate-300 dark:border-slate-600 rounded-full flex items-center justify-center text-slate-500 shadow-sm">
                                <BrainCircuit class="w-5 h-5" />
                            </div>
                            <h4 class="text-xl font-bold text-slate-900 dark:text-white mb-2">{{ tm('tech.journey.steps')[2].title }}</h4>
                            <p class="text-slate-600 dark:text-slate-400">{{ tm('tech.journey.steps')[2].desc }}</p>
                        </div>

                        <div class="relative">
                            <div class="absolute -left-[41px] top-0 w-10 h-10 bg-white dark:bg-atron-surface border-2 border-slate-300 dark:border-slate-600 rounded-full flex items-center justify-center text-slate-500 shadow-sm">
                                <DatabaseZap class="w-5 h-5" />
                            </div>
                            <h4 class="text-xl font-bold text-slate-900 dark:text-white mb-2">{{ tm('tech.journey.steps')[3].title }}</h4>
                            <p class="text-slate-600 dark:text-slate-400">{{ tm('tech.journey.steps')[3].desc }}</p>
                        </div>
                    </div>
                </div>

                <div>
                    <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-8 flex items-center gap-2">
                        <Layers class="text-atron-red" /> {{ t('tech.layers.title') }}
                    </h3>

                    <div class="space-y-4">
                        <div v-for="(layer, i) in tm('tech.layers.items')" :key="i"
                             class="group relative overflow-hidden bg-white dark:bg-atron-surface border border-slate-200 dark:border-slate-700 p-6 rounded-xl hover:border-atron-red/50 transition-colors shadow-sm">
                            
                            <div class="flex items-center justify-between relative z-10">
                                <div>
                                    <h4 class="font-bold text-slate-900 dark:text-white">{{ layer.name }}</h4>
                                    <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">{{ layer.desc }}</p>
                                </div>
                                <Server class="w-6 h-6 text-slate-300 dark:text-slate-600 group-hover:text-atron-red transition-colors" />
                            </div>

                            <div class="absolute inset-0 bg-gradient-to-r from-red-50 to-transparent dark:from-red-900/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
                        </div>
                    </div>
                    
                    <div class="mt-8 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg text-sm text-blue-800 dark:text-blue-200 flex gap-3">
                        <ShieldCheck class="w-5 h-5 flex-shrink-0" />
                        <p>
                            {{ locale === 'tr' ? 'Tüm katmanlar KVKK/GDPR uyumlu şekilde, isteğe bağlı On-premise veya Cloud olarak yapılandırılabilir.' : 'All layers are KVKK/GDPR compliant and can be deployed On-premise or Cloud based on your needs.' }}
                        </p>
                    </div>

                </div>

            </div>
        </div>
      </section>

      <section class="py-24 bg-white dark:bg-atron-dark transition-colors">
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
                            {{ locale === 'tr' ? 'Verimsizliği Bütçeye Dönüştürün.' : 'Turn Inefficiency into Budget.' }}
                        </h2>
                        <p class="text-lg text-white/90 mb-8 max-w-md">
                            {{ t('roi.subtitle') }}
                        </p>
                        <p class="text-xs text-white/60">
                            * {{ t('roi.note') }}
                        </p>
                    </div>

                    <div class="bg-white text-slate-900 p-8 rounded-2xl shadow-xl">
                        
                        <div class="mb-8">
                            <label class="block text-sm font-bold text-slate-500 mb-2 flex justify-between">
                                {{ t('roi.labels.agents') }}
                                <span class="text-atron-red text-lg font-black">{{ agentCount }}</span>
                            </label>
                            <input type="range" v-model="agentCount" min="5" max="500" step="5" class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-atron-red">
                        </div>

                        <div class="mb-10">
                            <label class="block text-sm font-bold text-slate-500 mb-2 flex justify-between">
                                {{ t('roi.labels.cost') }}
                                <span class="text-slate-900 font-bold">{{ agentCost.toLocaleString() }} TL</span>
                            </label>
                            <input type="range" v-model="agentCost" min="17002" max="100000" step="1000" class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-slate-900">
                        </div>

                        <div class="bg-slate-50 border border-slate-100 rounded-xl p-6 text-center">
                            <p class="text-slate-500 text-sm font-bold uppercase mb-1">{{ t('roi.labels.saved') }}</p>
                            <p class="text-4xl md:text-5xl font-black text-atron-red tracking-tight">
                                ₺{{ annualSavings }}
                            </p>
                            <div class="mt-4 inline-block bg-green-100 text-green-700 text-xs font-bold px-3 py-1 rounded-full">
                                {{ locale === 'tr' ? '%30 Verimlilik Artışı' : '30% Efficiency Gain' }}
                            </div>
                        </div>

                    </div>

                </div>
            </div>

        </div>
      </section>

      <footer id="contact" class="bg-slate-900 text-white pt-20 pb-10 border-t border-slate-800">
        <div class="container mx-auto px-4 md:px-6">
            
            <div class="grid md:grid-cols-2 gap-12 mb-16">
                <div>
                    <h2 class="text-5xl md:text-7xl font-black tracking-tighter text-white mb-6">
                        ATRON
                    </h2>
                    <p class="text-2xl md:text-3xl text-slate-400 font-light">
                        {{ t('footer.slogan') }} <br />
                        <span class="text-white font-bold">{{ t('footer.sub_slogan') }}</span>
                    </p>
                </div>

                <div class="flex flex-col justify-center items-start md:items-end space-y-6">
                    <a href="mailto:can@aiforpeople.co" class="group flex items-center gap-4 text-2xl font-bold hover:text-atron-red transition-colors">
                        <div class="w-12 h-12 rounded-full bg-slate-800 flex items-center justify-center group-hover:bg-atron-red group-hover:text-white transition-colors">
                            <Mail class="w-6 h-6" />
                        </div>
                        can@aiforpeople.co
                    </a>
                    
                    <div class="flex gap-4">
                        <a href="#" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-[#0077b5] hover:text-white transition-colors">
                            <Linkedin class="w-5 h-5" />
                        </a>
                        <a href="#" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-black hover:text-white transition-colors">
                            <Twitter class="w-5 h-5" />
                        </a>
                    </div>
                </div>
            </div>

            <div class="border-t border-slate-800 pt-8 flex flex-col md:flex-row justify-between items-center text-slate-500 text-sm">
                <p>&copy; {{ new Date().getFullYear() }} ATRON AI. {{ t('footer.rights') }}</p>
                <div class="flex gap-6 mt-4 md:mt-0">
                    <a href="#" class="hover:text-white transition-colors">{{ t('footer.links.privacy') }}</a>
                    <a href="#" class="hover:text-white transition-colors">{{ t('footer.links.terms') }}</a>
                </div>
            </div>

        </div>
      </footer>

    </main>

    <footer class="bg-slate-900 text-white py-8 text-center">
      <p>&copy; {{ new Date().getFullYear() }} ATRON AI Call Center.</p>
    </footer>

  </div>
</template>