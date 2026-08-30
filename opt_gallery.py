import os

for fpath in ['gallery.html', 'happybday/gallery.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add load more script and hide items initially
    style_patch = """
    .item {
      display: none; /* hidden by default */
    }
    .item.visible {
      display: inline-block;
      animation: fadeIn 0.5s ease;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .load-more-btn {
      display: block;
      margin: 20px auto 40px;
      padding: 12px 30px;
      font-size: 16px;
      font-weight: bold;
      color: #fff;
      background: linear-gradient(135deg, #ff69b4, #ff1493);
      border: none;
      border-radius: 25px;
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(255, 105, 180, 0.4);
      transition: transform 0.2s;
    }
    .load-more-btn:active { transform: scale(0.95); }
    .load-more-btn.hidden { display: none; }
    """
    
    if ".load-more-btn {" not in content:
        content = content.replace("    /* Lightbox */", style_patch + "\n    /* Lightbox */")
    
    script_patch = """
    let currentItemIndex = 0;
    const itemsPerLoad = 12;
    const allItems = document.querySelectorAll('.item');
    
    function loadMoreItems() {
      let loaded = 0;
      while (loaded < itemsPerLoad && currentItemIndex < allItems.length) {
        allItems[currentItemIndex].classList.add('visible');
        currentItemIndex++;
        loaded++;
      }
      if (currentItemIndex >= allItems.length) {
        const btn = document.getElementById('loadMoreBtn');
        if(btn) btn.classList.add('hidden');
      }
    }
    
    // Initial load
    document.addEventListener('DOMContentLoaded', () => {
      loadMoreItems();
    });
    """
    
    if "loadMoreItems()" not in content:
        content = content.replace("  </div>\n  \n  <div class=\"lightbox\"", "  </div>\n  <button id=\"loadMoreBtn\" class=\"load-more-btn\" onclick=\"loadMoreItems()\">Load More Memories ??</button>\n  \n  <div class=\"lightbox\"")
        content = content.replace("function openLightbox", script_patch + "\n    function openLightbox")
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Gallery optimized with Load More")
