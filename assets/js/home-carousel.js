// achievement-carousel.js
class AchievementCarousel {
  constructor(containerId, dataUrl) {
    this.container = document.getElementById(containerId);
    if (!this.container) {
      console.error(`Carousel container with ID "${containerId}" not found`);
      return;
    }
    
    // Add the achievement-carousel class for SCSS targeting
    this.container.classList.add('achievement-carousel');
    
    this.dataUrl = dataUrl;
    this.currentIndex = 0;
    this.achievements = [];
    this.isAnimating = false;
    this.touchStartX = 0;
    this.touchEndX = 0;
    this.autoSlideInterval = null;
    
    // Configuration
    this.config = {
      autoSlideInterval: 5000,
      swipeThreshold: 50,
      transitionDuration: 500,
      reducedMotion: window.matchMedia('(prefers-reduced-motion: reduce)').matches
    };
    
    this.init();
  }
  
  async init() {
    try {
      // Add loading state
      this.container.setAttribute('aria-busy', 'true');
      this.container.classList.add('loading');
      
      await this.loadData();
      
      // Remove loading state
      this.container.removeAttribute('aria-busy');
      this.container.classList.remove('loading');
      
      this.renderCarousel();
      this.setupEventListeners();
      
      // Only start auto-slide if user doesn't prefer reduced motion
      if (!this.config.reducedMotion) {
        this.startAutoSlide();
      }
      
    } catch (error) {
      console.error('Error initializing achievement carousel:', error);
      this.container.removeAttribute('aria-busy');
      this.container.classList.remove('loading');
      this.showErrorMessage();
    }
  }
  
  async loadData() {
    try {
      if (this.dataUrl) {
        const response = await fetch(this.dataUrl);
        
        if (!response.ok) {
          throw new Error(`Failed to load data: ${response.status} ${response.statusText}`);
        }
        
        const data = await response.json();
        
        if (!data.achievements || !Array.isArray(data.achievements)) {
          throw new Error('Invalid data format: missing achievements array');
        }
        
        // Process achievements
        this.achievements = data.achievements.map((achievement, index) => ({
          id: achievement.id || index + 1,
          tag: achievement.tag || '',
          title: achievement.title || '',
          description: achievement.description || '',
          imageUrl: achievement.imageUrl || this.getFallbackImage(index),
          link: achievement.link ? {
            text: achievement.link.text || 'Learn More',
            url: achievement.link.url || '#'
          } : null
        }));
        
      } else {
        // Fallback data
        this.achievements = this.getDefaultData();
      }
      
    } catch (error) {
      console.error('Error loading carousel data:', error);
      this.achievements = this.getDefaultData();
    }
  }
  
  getDefaultData() {
    return [
      {
        "id": 1,
        "tag": "AWARD",
        "title": "Eaton STAR Leadership in Data Science Award 2024",
        "description": "Received Eaton's prestigious STAR Leadership Award in Data Science for demonstrating outstanding leadership and excellence in advancing data science practices.",
        "imageUrl": "images/achievements/arts.jpg",
        "link": {
          "text": "",
          "url": ""
        }
      }
      // Add more achievements here if needed
    ];
  }
  
  getFallbackImage(index) {
    // Use your gradient colors from SCSS
    return `linear-gradient(135deg, ${this.getColor(index, 'start')} 0%, ${this.getColor(index, 'end')} 100%)`;
  }
  
  getColor(index, type) {
    const colors = [
      { start: '#FF777C', end: '#FCA5A5' }, // pink to pink-dark
      { start: '#1E293B', end: '#0369A1' }, // teal to cyan
      { start: '#10B981', end: '#8B5CF6' }, // energy-accent to ai-accent
      { start: '#2563EB', end: '#3C4F76' }  // blue to indigo
    ];
    const colorSet = colors[index % colors.length];
    return type === 'start' ? colorSet.start : colorSet.end;
  }
  
  renderCarousel() {
    if (!this.container || this.achievements.length === 0) {
      this.showEmptyState();
      return;
    }
    
    this.container.innerHTML = `
      <div class="carousel-track">
        ${this.achievements.map((achievement, index) => this.renderSlide(achievement, index)).join('')}
      </div>
      
      <button class="carousel-nav prev" 
        aria-label="Previous slide"
        ${this.achievements.length <= 1 ? 'disabled' : ''}>
        <i class="bi bi-chevron-left" aria-hidden="true"></i>
      </button>
      <button class="carousel-nav next" 
        aria-label="Next slide"
        ${this.achievements.length <= 1 ? 'disabled' : ''}>
        <i class="bi bi-chevron-right" aria-hidden="true"></i>
      </button>
      
      <div class="carousel-indicators" 
           role="tablist" 
           aria-label="Select a slide to display">
        ${this.achievements.map((_, index) => `
          <button class="indicator ${index === 0 ? 'active' : ''}" 
                  data-index="${index}"
                  role="tab"
                  aria-label="Slide ${index + 1}"
                  aria-selected="${index === 0}"
                  ${index === 0 ? 'tabindex="0"' : 'tabindex="-1"'}></button>
        `).join('')}
      </div>
      
      <div class="carousel-status" aria-live="polite" aria-atomic="true">
        <span class="sr-only">Slide ${this.currentIndex + 1} of ${this.achievements.length}</span>
      </div>
    `;
    
    // Cache DOM elements
    this.carouselTrack = this.container.querySelector('.carousel-track');
    this.indicators = this.container.querySelectorAll('.indicator');
    this.prevBtn = this.container.querySelector('.carousel-nav.prev');
    this.nextBtn = this.container.querySelector('.carousel-nav.next');
    this.carouselStatus = this.container.querySelector('.carousel-status');
    
    this.updateCarousel();
  }
  
  renderSlide(achievement, index) {
    const isActive = index === 0;
    const isImageUrl = achievement.imageUrl && 
                      (achievement.imageUrl.includes('http') || 
                       achievement.imageUrl.includes('/') || 
                       achievement.imageUrl.includes('.jpg') || 
                       achievement.imageUrl.includes('.png'));
    
    const backgroundStyle = isImageUrl ? 
      `background-image: url('${achievement.imageUrl}')` : 
      `background: ${achievement.imageUrl}`;
    
    return `
      <div class="carousel-slide" 
           data-index="${index}"
           role="tabpanel"
           aria-roledescription="slide"
           aria-label="${index + 1} of ${this.achievements.length}"
           ${isActive ? 'aria-current="true"' : 'aria-hidden="true"'}
           ${isActive ? 'tabindex="0"' : 'tabindex="-1"'}
           style="${backgroundStyle}">
        
        <div class="slide-content">
          <span class="slide-tag">${achievement.tag}</span>
          <h2 class="slide-title">${achievement.title}</h2>
          <p class="slide-description">${achievement.description}</p>
          ${achievement.link && achievement.link.url ? `
            <a href="${achievement.link.url}" class="btn btn-primary">
              ${achievement.link.text || 'Learn More'}
              <i class="bi bi-arrow-right" aria-hidden="true"></i>
            </a>
          ` : ''}
        </div>
      </div>
    `;
  }
  
  setupEventListeners() {
    if (this.achievements.length <= 1) return;
    
    // Indicators
    this.indicators.forEach(indicator => {
      indicator.addEventListener('click', (e) => {
        const index = parseInt(e.currentTarget.dataset.index);
        this.goToSlide(index);
      });
    });
    
    // Navigation buttons
    this.prevBtn.addEventListener('click', () => {
      this.prevSlide();
    });
    
    this.nextBtn.addEventListener('click', () => {
      this.nextSlide();
    });
    
    // Keyboard navigation
    this.container.addEventListener('keydown', (e) => {
      switch (e.key) {
        case 'ArrowLeft':
          e.preventDefault();
          this.prevSlide();
          break;
        case 'ArrowRight':
          e.preventDefault();
          this.nextSlide();
          break;
        case 'Home':
          e.preventDefault();
          this.goToSlide(0);
          break;
        case 'End':
          e.preventDefault();
          this.goToSlide(this.achievements.length - 1);
          break;
      }
    });
    
    // Mouse events
    this.container.addEventListener('mouseenter', () => {
      this.pauseAutoSlide();
    });
    
    this.container.addEventListener('mouseleave', () => {
      if (!this.config.reducedMotion) {
        this.resumeAutoSlide();
      }
    });
    
    // Touch events
    this.container.addEventListener('touchstart', (e) => {
      this.touchStartX = e.touches[0].clientX;
      this.pauseAutoSlide();
    }, { passive: true });
    
    this.container.addEventListener('touchend', (e) => {
      this.touchEndX = e.changedTouches[0].clientX;
      this.handleSwipe();
    }, { passive: true });
  }
  
  handleSwipe() {
    const diff = this.touchStartX - this.touchEndX;
    
    if (Math.abs(diff) > this.config.swipeThreshold) {
      if (diff > 0) {
        this.nextSlide();
      } else {
        this.prevSlide();
      }
    }
  }
  
  updateCarousel() {
    if (!this.carouselTrack || !this.indicators) return;
    
    // Update track position
    if (!this.config.reducedMotion) {
      this.carouselTrack.style.transition = `transform ${this.config.transitionDuration}ms ease-in-out`;
    } else {
      this.carouselTrack.style.transition = 'none';
    }
    
    this.carouselTrack.style.transform = `translateX(-${this.currentIndex * 100}%)`;
    
    // Update slides
    this.container.querySelectorAll('.carousel-slide').forEach((slide, index) => {
      const isActive = index === this.currentIndex;
      slide.setAttribute('aria-hidden', !isActive);
      slide.setAttribute('aria-current', isActive ? 'true' : 'false');
      slide.tabIndex = isActive ? 0 : -1;
    });
    
    // Update indicators
    this.indicators.forEach((indicator, index) => {
      const isActive = index === this.currentIndex;
      indicator.classList.toggle('active', isActive);
      indicator.setAttribute('aria-selected', isActive);
      indicator.tabIndex = isActive ? 0 : -1;
    });
    
    // Update status
    if (this.carouselStatus) {
      this.carouselStatus.innerHTML = `
        <span class="sr-only">
          Slide ${this.currentIndex + 1} of ${this.achievements.length}: 
          ${this.achievements[this.currentIndex]?.title || ''}
        </span>
      `;
    }
    
    // Update button states
    if (this.prevBtn && this.nextBtn) {
      this.prevBtn.disabled = this.currentIndex === 0;
      this.nextBtn.disabled = this.currentIndex === this.achievements.length - 1;
    }
  }
  
  goToSlide(index) {
    if (this.isAnimating || index === this.currentIndex || index < 0 || index >= this.achievements.length) {
      return;
    }
    
    this.isAnimating = true;
    this.currentIndex = index;
    this.updateCarousel();
    
    setTimeout(() => {
      this.isAnimating = false;
    }, this.config.transitionDuration);
  }
  
  nextSlide() {
    const nextIndex = (this.currentIndex + 1) % this.achievements.length;
    this.goToSlide(nextIndex);
  }
  
  prevSlide() {
    const prevIndex = this.currentIndex === 0 ? 
      this.achievements.length - 1 : 
      this.currentIndex - 1;
    this.goToSlide(prevIndex);
  }
  
  startAutoSlide() {
    if (this.achievements.length <= 1 || this.config.reducedMotion) return;
    
    this.pauseAutoSlide();
    
    this.autoSlideInterval = setInterval(() => {
      this.nextSlide();
    }, this.config.autoSlideInterval);
  }
  
  pauseAutoSlide() {
    if (this.autoSlideInterval) {
      clearInterval(this.autoSlideInterval);
      this.autoSlideInterval = null;
    }
  }
  
  resumeAutoSlide() {
    if (!this.autoSlideInterval && !this.config.reducedMotion && this.achievements.length > 1) {
      this.startAutoSlide();
    }
  }
  
  showErrorMessage() {
    this.container.innerHTML = `
      <div class="carousel-error">
        <p>Unable to load achievements. Please check your connection and try again.</p>
        <button class="btn btn-primary" onclick="location.reload()">Retry</button>
      </div>
    `;
  }
  
  showEmptyState() {
    this.container.innerHTML = `
      <div class="carousel-empty">
        <p>No achievements to display at the moment.</p>
      </div>
    `;
  }
  
  destroy() {
    this.pauseAutoSlide();
  }
}

// Quarto-safe initialization
function waitForAchievementCarousel() {
  const carouselContainer = document.getElementById('achievementCarousel');

  if (!carouselContainer) {
    // Quarto may not have rendered the HTML yet
    setTimeout(waitForAchievementCarousel, 50);
    return;
  }

  const dataUrl =
    carouselContainer.dataset.jsonUrl || 'data/achievements.json';

  try {
    window.achievementCarousel = new AchievementCarousel(
      'achievementCarousel',
      dataUrl
    );
  } catch (error) {
    console.error('Failed to initialize carousel:', error);
    carouselContainer.innerHTML = `
      <div class="carousel-error">
        <p>Failed to load carousel. Please refresh the page.</p>
        <button class="btn btn-primary" onclick="location.reload()">Retry</button>
      </div>
    `;
  }
}

// Start waiting for DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', waitForAchievementCarousel);
} else {
  waitForAchievementCarousel();
}