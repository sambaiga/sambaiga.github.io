// Reading progress indicators
document.addEventListener('DOMContentLoaded', function() {
  // Calculate reading progress based on reading time
  const readingTimeElements = document.querySelectorAll('.reading-time');
  
  readingTimeElements.forEach(el => {
    const text = el.textContent;
    const minutesMatch = text.match(/(\d+)\s*min/);
    
    if (minutesMatch) {
      const minutes = parseInt(minutesMatch[1]);
      const parentCard = el.closest('.blog-post');
      
      if (parentCard) {
        const progressBar = parentCard.querySelector('.reading-progress');
        if (progressBar) {
          // Simple progress calculation: 5% per minute, max 90%
          const progress = Math.min(minutes * 5, 90);
          progressBar.style.width = `${progress}%`;
        }
      }
    }
  });
});