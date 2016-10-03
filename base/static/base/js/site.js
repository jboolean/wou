var bindEvents = function() {
	var i;

	var elements = {
		mobileMenuButton: document.querySelector('.navicon'),
		mobileMenu: document.querySelector('.navigation'),
		mobileShowButtons: document.querySelectorAll('.facilitator-toggle'),
		scrollToAnchors: document.querySelectorAll('.navigation-menu-item a, .tool-facilitator, .tool-training'),
	};

	// mobile menu toggle
	elements.mobileMenuButton.addEventListener('click', function(e) {
		e.preventDefault();

		if (elements.mobileMenu.classList.contains('show')) {
			elements.mobileMenu.classList.remove('show');
		} else {
			elements.mobileMenu.classList.add('show');
		}
	});

	// scrolls
	for (i = 0; i < elements.scrollToAnchors.length; i++) {
		elements.scrollToAnchors[i].addEventListener('click', function(e) {
			e.preventDefault();
			elements.mobileMenu.classList.remove('show');

			Velocity(
				document.querySelector(this.getAttribute('href')),
				'scroll',
				{ duration: 300, offset: -40 }
			);
		});
	}

	// mobile facilitator show more
	for (i = 0; i < elements.mobileShowButtons.length; i++) {
		elements.mobileShowButtons[i].addEventListener('click', function(e) {
			e.preventDefault();
			this.parentElement.classList.add('show');
		});
	}
};

scrollToSlug = function() {
	var urlParts = window.location.href.split('/').filter(Boolean);

	if (urlParts.length > 2) {
		var slug = urlParts.pop();

		Velocity(
			document.querySelector('#' + slug),
			'scroll',
			{ duration: 0, offset: -40 }
		);
	}
};

document.addEventListener('DOMContentLoaded', function() {
	scrollToSlug();
	bindEvents();
});

