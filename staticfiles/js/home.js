
const light = document.querySelector(".cursor-light");
document.addEventListener("mousemove", (e) => {
    light.style.left = e.clientX + "px";
    light.style.top = e.clientY + "px";
});

const navLinks = document.querySelectorAll('.nav-anim');
const sections = document.querySelectorAll('section[id]');

navLinks.forEach(link => {
    link.addEventListener('click', function (e) {
        navLinks.forEach(l => l.classList.remove('active'));
        this.classList.add('active');
    });
});

function activateNavOnScroll() {
    let currentSection = '';
    const scrollPosition = window.scrollY + 200;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        const sectionId = section.getAttribute('id');

        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            currentSection = sectionId;
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentSection}`) {
            link.classList.add('active');
        }
    });
}

window.addEventListener('scroll', activateNavOnScroll);

activateNavOnScroll();

function showMessage(message, type = 'success') {
    const toast = document.getElementById('liveToast');
    const toastMessage = document.getElementById('toastMessage');

    toast.classList.remove('bg-success', 'bg-danger', 'bg-info');
    toastMessage.textContent = message;
    if (type == 'success') {
        toast.classList.add('bg-success');
    } else if (type == 'error') {
        toast.classList.add('bg-danger');
    } else if (type == 'info') {
        toast.classList.add('bg-info');
    }

    const Toast = new bootstrap.Toast(toast);
    Toast.show();
}
// get csrf token
function getCookie(val) {
    let cookie = null;
    if (document.cookie && document.cookie != null) {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const x = cookies[i].trim();
            const cur = x.substring(0, val.length + 1);
            if (cur == (val + '=')) {
                cookie = x.substring(cur.length);
                cookie = decodeURIComponent(cookie);
                break;
            }
        }
    }
    return cookie;
}
const form = document.querySelector('.contact-form');
form.addEventListener('submit', function (event) {
    event.preventDefault()
    const formData=new FormData(form)
    fetch(`/contact/contact_msg/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body:formData
    }).then(response => response.json()).then(data => {
        console.log('Response data:', data);
        if (data.success) {
            console.log('success:',data.success);
            showMessage(data.message, 'success');
            setTimeout(()=>location.reload(),3000);
        } else {
            showMessage(data.message, 'error');
        }
    });
});
