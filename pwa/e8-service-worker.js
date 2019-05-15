self.addEventListener("fetch", function(event){
  let pedido = event.request
  console.log("Tentou carregar alguma coisa")
  let promiseResposta = caches.open("ceep-imagens").then(cache => {
    return cache.match(pedido)
  }).then(resposta =>{
      return resposta
    })
  event.respondWith(promiseResposta)
})
