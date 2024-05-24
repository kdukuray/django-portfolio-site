// function that makes the home page (index.html) scrollable
const nav_links_on_home_page = document.querySelectorAll("a[href^='#']");
nav_links_on_home_page.forEach(link => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
        document.querySelector(e.currentTarget.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});

// function for intersection observer which allows for the fade in effect
const observer = new IntersectionObserver(entries => {
    entries.forEach((entry) =>{
        if (entry.isIntersecting){
            entry.target.classList.add("show");
        }
        else{
            entry.target.classList.remove("show");
        }
    })
})
const hiddenElements = document.querySelectorAll(".hidden");
hiddenElements.forEach((el) => observer.observe(el));

// function to toggle admin pop up when user is authenticated
function toggle_admin_pop_up(){
    const pop_up = document.querySelector("#admin-dashboard-pop-up");
    pop_up.classList.toggle("hide");
}

// function that retrieves user input (in markdown) in order to render preview (About page)
function renderHtmlAboutPage(target_indetifier){
    let converter = new showdown.Converter();
    let post_body = document.querySelector("textarea");
    let all_text = post_body.value;
    all_text = converter.makeHtml(all_text);

    let post_preview = document.querySelector(target_indetifier);
    post_preview.innerHTML = all_text;

}

// function that takes beginning of button class-name as input, and either hides or displays all the buttons that match
function toggle_all_btn(class_begin){
    const all_delete_btns = document.querySelectorAll("a[class ^='" + class_begin + "']");
    all_delete_btns.forEach(btn=>{
        btn.classList.toggle("hide");
    })

}

// function that retrieves user input (in markdown) in order to render preview (Post page)
function renderHtml(target_indetifier){
    let converter = new showdown.Converter();
    let post_title = document.querySelector("input");

    let post_body = document.querySelector("textarea");
    let all_text = "#" + post_title.value + "\n" + post_body.value;
    all_text = converter.makeHtml(all_text);

    let post_preview = document.querySelector(target_indetifier);
    post_preview.innerHTML = all_text;
    Prism.highlightAll();
}

// function that creates pop up in order to confirm the deletion of a skill object
 function skillDeleteConfirmation(e, skillId){
    //Add back drop style to the page
    document.querySelector(".skills-page-section-container").classList.add("backdrop")

    //Retrieve details about the skill to be deleted
    let parent_element = e.target.parentElement
    let skill_img_url = parent_element.querySelector(".skill-logo")["src"]
    let skill_name = parent_element.querySelector(".skill-name").textContent
    //let csrf_token = parent_element.querySelector("input[name='csrfmiddlewaretoken']").value
    let csrf_token = document.querySelector("#csrf-token-container input[name='csrfmiddlewaretoken']").value

    //Actual confirmation form
    let deleteConfirmationForm = `
    <div class="skill-deletion-confirmation">
        <p>Are you sure you want to delete this:</p>
        <div class="individual-skill">
            <img src="${skill_img_url}" class="skill-logo">
            <p class="skill-name">${skill_name}</p>
        </div>
        <img src="${xBtn_url}" class="cancel-skill-delete-confirmation-btn">
    <form method="POST" action="${skillDeleteUrl}${skillId}/">
        <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
        <button>Delete</button>
    </form>

    </div>
    `;

    document.querySelector(".skills-page-content").innerHTML = deleteConfirmationForm + document.querySelector(".skills-page-content").innerHTML;
    document.querySelector(".cancel-skill-delete-confirmation-btn").addEventListener("click", () => cancelSkillDeleteConfirmation(event))

}

// function that cancels the deletion confirmation of a skill object
function cancelSkillDeleteConfirmation(e){
    document.querySelector(".skills-page-section-container").classList.remove("backdrop")
    let parent_element = e.target.parentElement
    parent_element.remove()
}

// function that creates pop up in order to confirm the deletion of a education object
function educationDeleteConfirmation(e, educationId){
    //Add back drop style to the page
    document.querySelector(".education-section-horizontal-bar").classList.add("backdrop")

    //Retrieve details about the skill to be deleted
    let parent_element = e.target.parentElement

    let education_title = parent_element.querySelector(".education-section-item-heading").textContent
    let education_year = parent_element.querySelector(".education-section-item-year").textContent
    let education_description = parent_element.querySelector(".education-section-item-description").textContent
    //let csrf_token = parent_element.querySelector("input[name='csrfmiddlewaretoken']").value
    let csrf_token = document.querySelector("#csrf-token-container input[name='csrfmiddlewaretoken']").value
    //Actual confirmation form
    let deleteConfirmationForm = `
     <div class="education-deletion-confirmation">
            <p>Are you sure you want to delete this:</p>
            <div class="education-section-item">
                <p class="education-section-item-heading">${education_title}</p>
                <p class="education-section-item-year">${education_year}</p>
                <p class="education-section-item-description">${education_description}</p>
                <a href="#" class="crud-delete-btn hide">Delete</a>
                <a href="#" class="crud-edit-btn hide">Edit</a>
            </div>
            <img src="${xBtn_url}" class="cancel-education-delete-confirmation-btn">
        <form method="POST" action="${educationDeleteUrl}${educationId}/">
            <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
            <button>Delete</button>
        </form>

    </div>

`;

    document.querySelector("#education-page-content").innerHTML = deleteConfirmationForm + document.querySelector("#education-page-content").innerHTML;
    document.querySelector(".cancel-education-delete-confirmation-btn").addEventListener("click", () => cancelEducationDeleteConfirmation(event))

}

// function that cancels the deletion confirmation of an education object
function cancelEducationDeleteConfirmation(e){
    document.querySelector(".education-section-horizontal-bar").classList.remove("backdrop")
    let parent_element = e.target.parentElement
    parent_element.remove()
}



// function that creates pop up in order to confirm the deletion of a post object
function postDeleteConfirmation(e, postId){
    //Add back drop style to the page
    document.querySelector(".single-post-page-content").classList.add("backdrop")

    let csrf_token = document.querySelector("#csrf-token-container input[name='csrfmiddlewaretoken']").value
    //Actual confirmation form
    let deleteConfirmationForm = `
     <div class="post-deletion-confirmation">
                <p>Are you sure you want to delete this post:</p>
                <img src="${xBtn_url}" class="cancel-post-delete-confirmation-btn">
            <form method="POST" action="${postDeleteUrl}${postId}/">
            <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
                <button>Delete</button>
            </form>
            </div>

`;

    document.querySelector("#page-content").innerHTML = deleteConfirmationForm + document.querySelector("#page-content").innerHTML;
    document.querySelector(".cancel-post-delete-confirmation-btn").addEventListener("click", () => cancelPostDeleteConfirmation(event))
}

// function that cancels the deletion confirmation of a post object
function cancelPostDeleteConfirmation(e){
    document.querySelector(".single-post-page-content").classList.remove("backdrop")
    let parent_element = e.target.parentElement
    parent_element.remove()
}

// function that creates pop up in order to confirm the deletion of a message object
function messageDeleteConfirmation(e, messageId){
    //Add back drop style to the page
    document.querySelector(".single-message-page-content").classList.add("backdrop")

    let csrf_token = document.querySelector("#csrf-token-container input[name='csrfmiddlewaretoken']").value
    //Actual confirmation form
    let deleteConfirmationForm = `
     <div class="post-deletion-confirmation">
                <p>Are you sure you want to delete this post:</p>
                <img src="${xBtn_url}" class="cancel-message-delete-confirmation-btn">
            <form method="POST" action="${messageDeleteUrl}${messageId}/">
            <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}">
                <button>Delete</button>
            </form>
            </div>

`;

    document.querySelector("#page-content").innerHTML = deleteConfirmationForm + document.querySelector("#page-content").innerHTML;
    document.querySelector(".cancel-message-delete-confirmation-btn").addEventListener("click", () => cancelMessageDeleteConfirmation(event))
}

// function that cancels the deletion confirmation of a Message object
function cancelMessageDeleteConfirmation(e){
    document.querySelector(".single-message-page-content").classList.remove("backdrop")
    let parent_element = e.target.parentElement
    parent_element.remove()
}

// function that handles sending new messages to the save message route
// Adds and removes loading spinner to form as necessary
// includes timing delay function so that the spinner is visible for a minimum of 1s
// includes additional delay function so that the message is visible to the user for at least 3s
async function submit_message_form(e){
    e.preventDefault();
    const spinner = document.querySelector(".loading-spinner");
    const form = document.querySelector(".contact-form");
    spinner.style.display = "block";
    spinner.style.animationPlayState = "running";
    form.style.opacity = "30%";
    const submitMessageUrl = document.querySelector(".contact-form")["action"]
    const sender_name = form.querySelector("input[name='name']").value
    const sender_email = form.querySelector("input[name='email']").value
    let csrf_token = form.querySelector("input[name='csrfmiddlewaretoken']").value
    const content = form.querySelector("textarea").value

    let message = document.createElement("div");

    let payload = new URLSearchParams();
    payload.append("sender_name", sender_name);
    payload.append("sender_email", sender_email);
    payload.append("content", content);

    await fetch(submitMessageUrl, {
    "method": "POST",
    "headers": {
            "Content-type": "application/x-www-form-urlencoded",
            "X-CSRFToken": csrf_token
    },
    "body": payload
    }).then( () => {
        message.innerHTML = "Your message has been sent succesfully!";
        form.querySelector("input[name='name']").value = ""
        form.querySelector("input[name='email']").value = ""
        form.querySelector("textarea").value = ""

    })
    .catch((error) =>{
        message.innerHTML = "There was an Error. Your message could not be sent!";
    })

    message.classList.add("message-status");
    await delay(1000);
    spinner.style.animationPlayState = "paused";
    spinner.style.display = "none";
    form.style.opacity = "100%";
    form.append(message);
    await delay(3000);
    message.style.display = "none";
    form.removeChild(message);

}

// simple delay function
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
