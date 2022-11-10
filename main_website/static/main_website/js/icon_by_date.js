let logo = document.getElementById("logo");

const refreshStatus = () => {
  // Get dates/time/hours
  let today = new Date(); // Todays date

  // Show available if this matches
  if (today.getMonth() == 10) {
    logo.src='/static/main_website/img/scout_remembrance.png';
    logo.style.width = "45px";
    logo.style.height = "45px";
  } else if (today.getMonth() == 11) {
    logo.src='/static/main_website/img/scout_christmas.png';
    logo.style.width = "35px";
    logo.style.height = "35px";
  } else {
    logo.src='/static/main_website/img/scout_logo_alt.png';
    logo.style.width = "35px";
    logo.style.height = "35px";
  }
}

// Run when starting
refreshStatus();

// Updates every 8 seconds
setInterval(refreshStatus, 8000);