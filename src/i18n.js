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

const i18n = createI18n({
  legacy: false,
  locale: 'tr',
  fallbackLocale: 'en',
  globalInjection: true,
  messages
});

export default i18n;