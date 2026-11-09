// Comportamentos pequenos, todos opcionais: sem JavaScript o site funciona e mostra tudo.

/* ---- tema: segue o sistema até a pessoa escolher; a escolha fica salva ---- */
const root = document.documentElement
const systemLight = window.matchMedia('(prefers-color-scheme: light)')
const current = () => root.dataset.theme || (systemLight.matches ? 'light' : 'dark')

document.querySelector('.theme-toggle')?.addEventListener('click', () => {
  const next = current() === 'dark' ? 'light' : 'dark'
  root.dataset.theme = next
  try {
    localStorage.setItem('theme', next)
  } catch (e) {
    /* navegação privada: vale só nesta visita */
  }
})

/* ---- aparece ao rolar; com "reduzir animações" o CSS já mostra tudo ---- */
const items = document.querySelectorAll('.reveal')
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible')
          io.unobserve(entry.target)
        }
      }
    },
    { rootMargin: '0px 0px -8% 0px', threshold: 0.08 }
  )
  items.forEach((el) => io.observe(el))
} else {
  items.forEach((el) => el.classList.add('is-visible'))
}
