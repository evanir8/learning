//navigator.serviceWorker.register('/e8-service-worker.js');
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/e8-service-worker.js');
  });
}
