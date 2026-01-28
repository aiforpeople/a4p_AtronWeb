import { createApp } from 'vue'
import { createI18n } from 'vue-i18n'
import './style.css'
import App from './App.vue'

import tr from './locales/tr.json'
import en from './locales/en.json'

const i18n = createI18n({
  legacy: false, 
  locale: 'tr', 
  fallbackLocale: 'en',
  messages: { tr, en }
})

createApp(App)
  .use(i18n)
  .mount('#app')