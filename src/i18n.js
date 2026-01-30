import { createI18n } from 'vue-i18n';

const messages = Object.fromEntries(
  Object.entries(
    import.meta.glob('./locales/*.json', { eager: true })
  ).map(([key, value]) => {
    const matched = key.match(/\.\/locales\/(.*)\.json/);
    return [matched[1], value.default];
  })
);

export const availableLocales = Object.keys(messages);

function getBrowserLocale() {
  try {
    if (typeof navigator !== 'undefined') {
      const browserLang = navigator.language || navigator.userLanguage; 
      const userLangShort = browserLang.split('-')[0];
      if (availableLocales.includes(userLangShort)) {
        return userLangShort;
      }
    }
  } catch (e) {
    console.warn('Error detecting browser locale:', e);
  }
  return 'en';
}

const i18n = createI18n({
  legacy: false,
  locale: getBrowserLocale(),
  fallbackLocale: 'en',
  globalInjection: true,
  messages
});

export default i18n;