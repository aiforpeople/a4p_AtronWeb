<script setup>
import { useI18n } from 'vue-i18n';
import { Mail, PhoneIncoming, Linkedin, Twitter } from 'lucide-vue-next';
const { t } = useI18n();
</script>

<template>
  <footer id="contact" class="bg-slate-900 text-white pt-20 pb-10 border-t border-slate-800">
    <div class="container mx-auto px-4 md:px-6">
        <div class="grid md:grid-cols-2 gap-12 mb-16">
            <div>
                <h2 class="text-5xl md:text-7xl font-black tracking-tighter text-white mb-6">ATRON</h2>
                <p class="text-2xl md:text-3xl text-slate-400 font-light">
                    {{ t('footer.slogan') }} <br />
                    <span class="text-white font-bold">{{ t('footer.sub_slogan') }}</span>
                </p>
            </div>

            <div class="flex flex-col justify-center items-start md:items-end space-y-6">
                <a href="mailto:info@aiforpeople.co" class="group flex items-center gap-4 text-2xl font-bold hover:text-atron-red transition-colors">
                    <div class="w-12 h-12 rounded-full bg-slate-800 flex items-center justify-center group-hover:bg-atron-red group-hover:text-white transition-colors">
                        <Mail class="w-6 h-6" />
                    </div>
                    info@aiforpeople.co
                </a>

                <a href="tel:+908505329105" class="group flex items-center gap-4 text-2xl font-bold hover:text-atron-red transition-colors">
                    <div class="w-12 h-12 rounded-full bg-slate-800 flex items-center justify-center group-hover:bg-atron-red group-hover:text-white transition-colors">
                        <PhoneIncoming class="w-6 h-6" />
                    </div>
                    &nbsp; +90 (850) 532 91 05
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
                <router-link :to="{ name: 'privacy' }" class="hover:text-white transition-colors">
                {{ t('footer.links.privacy') }}
                </router-link>
                <router-link :to="{ name: 'terms' }" class="hover:text-white transition-colors">
                {{ t('footer.links.terms') }}
                </router-link>
            </div>
        </div>
    </div>
  </footer>
</template>