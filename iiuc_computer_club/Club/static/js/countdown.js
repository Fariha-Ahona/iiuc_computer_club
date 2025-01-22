// Set the date and time for the seminar
const seminarDate = new Date(2024, 12, 31, 10, 0, 0); // Year, Month (0-indexed), Day, Hour, Minute, Second
 // +06:00 is the offset for Bangladesh
 // Replace with your event's date and time

function updateCountdown() {
  const now = new Date();
  const timeDifference = seminarDate - now;

  if (timeDifference <= 0) {
    document.getElementById("countdown-timer").innerHTML = "<p>🎉 The event has started!</p>";
    return;
  }

  const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
  const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

  document.getElementById("days").innerText = days;
  document.getElementById("hours").innerText = hours;
  document.getElementById("minutes").innerText = minutes;
  document.getElementById("seconds").innerText = seconds;
}

// Update the countdown every second
setInterval(updateCountdown, 1000);
updateCountdown(); // Call it once to avoid waiting 1 second for the first update


document.addEventListener("DOMContentLoaded", function () {
  updateCountdown();
  setInterval(updateCountdown, 1000);
});