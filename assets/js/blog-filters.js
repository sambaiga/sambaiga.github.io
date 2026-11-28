// Simple blog filtering
document.addEventListener('DOMContentLoaded', function() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  if (!filterButtons.length) return;
  
  filterButtons.forEach(button => {
    button.addEventListener('click', function() {
      // Remove active class from all buttons
      filterButtons.forEach(btn => btn.classList.remove('active'));
      
      // Add active class to clicked button
      this.classList.add('active');
      
      // Get filter value
      const filterValue = this.dataset.filter;
      
      // Get all blog posts
      const posts = document.querySelectorAll('.blog-post');
      
      // Show/hide posts based on filter
      posts.forEach(post => {
        const categories = post.dataset.categories || '';
        
        if (filterValue === 'all' || categories.includes(filterValue)) {
          post.style.opacity = '1';
          post.style.pointerEvents = 'auto';
          post.style.transform = 'scale(1)';
        } else {
          post.style.opacity = '0.3';
          post.style.pointerEvents = 'none';
          post.style.transform = 'scale(0.95)';
        }
      });
    });
  });
});