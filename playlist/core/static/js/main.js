const currentUrl = window.location.href;

const url = new URL(currentUrl);

const queryParams = url.searchParams;

const pageParam = queryParams.get('page') || "1";

if (pageParam !== null) {
    const pageLink = document.querySelector(`.page a[href="?page=${pageParam}"]`);
    if(pageLink) pageLink.parentElement.classList.add("active");
} 

const inputs = document.querySelectorAll('.input-form');

function addClassOnLabel(event){
    const label = event.currentTarget.parentElement.querySelector('.input-label');
    if(!label) return null;
    label.style.top = "-15px";
}

if(inputs){
    inputs.forEach(input => {
        if(input.value){
            const label = input.parentElement.querySelector('.input-label');
            if(!label) return null;
            label.style.top = "-15px";
        }
        input.addEventListener('keydown', addClassOnLabel)
        input.addEventListener('click', addClassOnLabel)
        input.addEventListener('blur', event => {
            const label = event.currentTarget.parentElement.querySelector('.input-label');
            if(!label) return null;
            if(!event.currentTarget.value) label.style.top = "10px";
        });
    });
}
