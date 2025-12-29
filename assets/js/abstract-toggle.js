// assets/js/abstract-toggle.js
document.addEventListener('DOMContentLoaded', function() {
  // Function to handle abstract toggle
  function handleAbstractToggle(event) {
    event.stopPropagation();
    
    const button = event.currentTarget;
    const abstractContent = button.closest('.abstract-content');
    const abstractRemainder = abstractContent.querySelector('.abstract-remainder');
    const abstractEllipsis = abstractContent.querySelector('.abstract-ellipsis');
    const readMoreText = button.querySelector('.read-more-text');
    const readMoreIcon = button.querySelector('.read-more-icon i');
    
    if (!abstractRemainder || !readMoreText) return;
    
    // Check current state
    const isExpanded = abstractRemainder.style.display === 'inline' || 
                      button.classList.contains('expanded');
    
    if (isExpanded) {
      // Collapse
      abstractRemainder.style.display = 'none';
      if (abstractEllipsis) abstractEllipsis.style.display = 'inline';
      readMoreText.textContent = 'Read more';
      button.classList.remove('expanded');
      abstractContent.classList.remove('expanded');
      if (readMoreIcon) {
        readMoreIcon.classList.remove('bi-chevron-up');
        readMoreIcon.classList.add('bi-chevron-down');
      }
    } else {
      // Expand
      abstractRemainder.style.display = 'inline';
      if (abstractEllipsis) abstractEllipsis.style.display = 'none';
      readMoreText.textContent = 'Read less';
      button.classList.add('expanded');
      abstractContent.classList.add('expanded');
      if (readMoreIcon) {
        readMoreIcon.classList.remove('bi-chevron-down');
        readMoreIcon.classList.add('bi-chevron-up');
      }
    }
  }
  
  // Initialize abstract toggle buttons
  function initAbstractToggle() {
    const toggleButtons = document.querySelectorAll('.abstract-read-more');
    
    toggleButtons.forEach(button => {
      // Remove existing listeners
      button.removeEventListener('click', handleAbstractToggle);
      button.addEventListener('click', handleAbstractToggle);
    });
  }
  
  // Initialize on page load
  initAbstractToggle();
  
  // Re-initialize when DOM changes
  const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      if (mutation.addedNodes.length) {
        setTimeout(initAbstractToggle, 50);
      }
    });
  });
  
  observer.observe(document.body, { childList: true, subtree: true });
});