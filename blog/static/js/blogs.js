document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();

      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        smoothScrollTo(target);
      }
    });
  });

  function smoothScrollTo(target) {
    const startPosition = window.pageYOffset;
    const targetPosition = target.getBoundingClientRect().top;
    const startTime = performance.now();

    function scrollAnimation(currentTime) {
      const timeElapsed = currentTime - startTime;
      const run = easeInOutQuad(
        timeElapsed,
        startPosition,
        targetPosition,
        1000
      );
      window.scrollTo(0, run);

      if (timeElapsed < 1000) {
        requestAnimationFrame(scrollAnimation);
      }
    }

    function easeInOutQuad(t, b, c, d) {
      t /= d / 2;
      if (t < 1) return (c / 2) * t * t + b;
      t--;
      return (-c / 2) * (t * (t - 2) - 1) + b;
    }

    requestAnimationFrame(scrollAnimation);
  }
});

//Pop up

jQuery(document).ready(function () {
  jQuery(".product").click(function () {
    var targetPopup = jQuery(this).data("popup-target");
    jQuery("#" + targetPopup).fadeIn();
    jQuery("body").addClass("hiiden-f").css("overflow", "hidden");
  });

  jQuery(".popup-div a").click(function () {
    jQuery(".popup-div").fadeOut();
    jQuery("body").removeClass("hiiden-f").css("overflow", "auto");
  });
});

// Darkmode button

document.addEventListener("DOMContentLoaded", function () {
  function initializeDarkModeButton(cardId) {
    const darkModeButton = document.querySelector(
      `#${cardId} .dark-mode-button`
    );
    const modeIcon = document.querySelector(`#${cardId} .mode-icon`);
    const modeIndicator = document.querySelector(`#${cardId} .mode-indicator`);
    const popupContent = document.querySelector(`#${cardId} .popup-content`);

    darkModeButton.addEventListener("click", function () {
      // Toggle dark mode class on the popup content for the specified card
      popupContent.classList.toggle("dark-mode");

      // Toggle text and icon on the button based on the current mode
      const isDarkMode = popupContent.classList.contains("dark-mode");
      modeIndicator.textContent = isDarkMode ? "☀️" : "🌑";
      modeIcon.innerHTML = isDarkMode
        ? '<i class="fas fa-moon"></i>'
        : '<i class="fas fa-sun"></i>';

      // You can add additional logic to toggle other dark mode elements here
    });
  }

  // Initialize dark mode button for Card - 1
  initializeDarkModeButton("popup-1");
  initializeDarkModeButton("popup-2");
  // Repeat for other cards as needed
});
