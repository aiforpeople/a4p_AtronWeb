<script setup>
import { computed } from 'vue';
import { useI18n } from 'vue-i18n';
import { 
  ArrowRight, ShieldCheck, 
  PhoneCall, AudioWaveform, Brain, FileCheck,
  Globe, MessageSquareText, Cpu, Database, Lock
} from 'lucide-vue-next';

const { t, tm } = useI18n();

const steps = computed(() => {
  const items = tm('tech.journey.steps');
  return Array.isArray(items) ? items : [];
});

const layers = computed(() => {
  const items = tm('tech.layers.items');
  return Array.isArray(items) ? items : [];
});

const stackIcons = [Globe, MessageSquareText, Cpu, Database, Lock];
</script>

<template>
  <section id="architecture" class="py-24 bg-slate-50 dark:bg-slate-900/50 relative overflow-hidden transition-colors duration-300">
    
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
                <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-10 flex items-center gap-2">
                    <ArrowRight class="text-atron-red" /> {{ t('tech.journey.title') }}
                </h3>
                
                <div class="space-y-8">
                    <div v-for="(step, index) in steps" :key="index" class="flex gap-6 relative group">
                        
                        <div class="flex-shrink-0 w-14 h-14 rounded-2xl flex items-center justify-center shadow-md transition-all duration-300 group-hover:scale-110"
                             :class="index === 0 
                                ? 'bg-atron-red text-white shadow-red-500/30' 
                                : 'bg-white dark:bg-atron-surface border border-slate-100 dark:border-slate-700 text-slate-500 dark:text-slate-400'">
                            
                            <PhoneCall v-if="index===0" class="w-6 h-6" />
                            <AudioWaveform v-else-if="index===1" class="w-6 h-6" />
                            <Brain v-else-if="index===2" class="w-6 h-6" />
                            <FileCheck v-else class="w-6 h-6" />
                        </div>

                        <div>
                            <h4 class="text-xl font-bold text-slate-900 dark:text-white mb-2 transition-colors">{{ step.title }}</h4>
                            <p class="text-slate-600 dark:text-slate-400 leading-relaxed transition-colors">{{ step.desc }}</p>
                        </div>
                    </div>
                </div>
            </div>

            <div>
                <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-8 flex items-center gap-2">
                    <component :is="Database" class="text-atron-red w-6 h-6" /> {{ t('tech.layers.title') }}
                </h3>

                <div class="space-y-4">
                    <div v-for="(layer, i) in layers" :key="i"
                         class="group relative overflow-hidden p-6 rounded-xl border transition-all duration-300 shadow-sm
                                bg-white dark:bg-slate-800 
                                border-slate-200 dark:border-slate-700
                                hover:border-atron-red dark:hover:border-atron-red">
                        
                        <div class="flex items-center justify-between relative z-10">
                            <div>
                                <h4 class="font-bold text-slate-900 dark:text-white transition-colors">{{ layer.name }}</h4>
                                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1 transition-colors">{{ layer.desc }}</p>
                            </div>
                            
                            <component :is="stackIcons[i]" class="w-6 h-6 text-slate-300 dark:text-slate-600 group-hover:text-atron-red transition-colors" />
                        </div>

                        <div class="absolute inset-0 bg-gradient-to-r from-red-50 to-transparent dark:from-red-900/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
                    </div>
                </div>
                
                <div class="mt-8 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg text-sm text-blue-800 dark:text-blue-200 flex gap-3 border border-blue-100 dark:border-blue-800">
                    <ShieldCheck class="w-5 h-5 flex-shrink-0" />
                    <p>{{ t('tech.compliance') }}</p>
                </div>
            </div>

        </div>
    </div>
  </section>
</template>