intents = {

# ===================== GREETINGS (1–10) =====================
"greeting": {
    "patterns": ["hi", "hello", "hey"],
    "response": "Hello! 👋 Welcome to Prince Travels ✈️. How can I help you?"
},

"good_morning": {
    "patterns": ["good morning"],
    "response": "Good morning ☀️! Ready to plan your journey?"
},

"good_evening": {
    "patterns": ["good evening"],
    "response": "Good evening 🌆! How may I assist you?"
},

"how_are_you": {
    "patterns": ["how are you"],
    "response": "I’m doing great 😊 and ready to help you travel!"
},

"bot_name": {
    "patterns": ["your name", "who are you"],
    "response": "I’m the Prince Travels virtual assistant 🤖✈️."
},

"help": {
    "patterns": ["help me", "need help"],
    "response": "Sure 👍 I can help with flights, hotels, cabs, and packages."
},

"thanks": {
    "patterns": ["thanks", "thank you"],
    "response": "You're welcome 🙏 Happy to help!"
},

"welcome_reply": {
    "patterns": ["nice", "great"],
    "response": "Glad you liked it 😊"
},

"goodbye": {
    "patterns": ["bye", "goodbye"],
    "response": "Thank you for choosing Prince Travels 👑✈️. Have a great day!"
},

"see_you": {
    "patterns": ["see you"],
    "response": "See you soon 👋 Safe travels!"
},

# ===================== FLIGHTS (11–40) =====================
"book_flight": {
    "patterns": ["book flight", "flight booking"],
    "response": "Sure ✈️ Please share your destination."
},

"cheap_flight": {
    "patterns": ["cheap flight", "low cost flight"],
    "response": "I’ll find the cheapest flight for you 💸✈️."
},

"international_flight": {
    "patterns": ["international flight"],
    "response": "We provide international flight bookings 🌍."
},

"domestic_flight": {
    "patterns": ["domestic flight"],
    "response": "Domestic flights are available across India 🇮🇳."
},

"cancel_flight": {
    "patterns": ["cancel flight"],
    "response": "Your flight cancellation request ❌✈️ is being processed."
},

"reschedule_flight": {
    "patterns": ["reschedule flight", "change flight"],
    "response": "Please share your booking ID 📄 to reschedule."
},

"flight_status": {
    "patterns": ["flight status"],
    "response": "Please provide your flight number ✈️."
},

"flight_delay": {
    "patterns": ["flight delayed"],
    "response": "Let me check the latest update ⏱️."
},

"baggage": {
    "patterns": ["baggage allowance"],
    "response": "Baggage allowance depends on airline ✈️."
},

"extra_baggage": {
    "patterns": ["extra baggage"],
    "response": "Extra baggage can be added during booking 🧳."
},

"seat_selection": {
    "patterns": ["seat selection"],
    "response": "You can choose window or aisle seats 💺."
},

"meal": {
    "patterns": ["meal", "food in flight"],
    "response": "Veg 🥗 and non-veg 🍗 meals are available."
},

"web_checkin": {
    "patterns": ["web check in"],
    "response": "Web check-in opens 24–48 hours before departure ✔️."
},

"boarding_pass": {
    "patterns": ["boarding pass"],
    "response": "You can download your boarding pass after check-in 🎫."
},

"flight_price": {
    "patterns": ["flight price"],
    "response": "Prices depend on date 📅 and availability."
},

"round_trip": {
    "patterns": ["round trip"],
    "response": "Round-trip flights are available 🔁✈️."
},

"one_way": {
    "patterns": ["one way flight"],
    "response": "One-way flight booking available ➡️✈️."
},

"last_minute_flight": {
    "patterns": ["last minute flight"],
    "response": "I’ll try to find last-minute deals 🕒."
},

"early_booking": {
    "patterns": ["advance booking"],
    "response": "Early bookings get better prices 💰."
},

"flight_support": {
    "patterns": ["flight help"],
    "response": "I’m here to assist with flight queries ✈️."
},

# ===================== HOTELS (41–65) =====================
"book_hotel": {
    "patterns": ["book hotel"],
    "response": "Sure 🏨 Please share your destination."
},

"cheap_hotel": {
    "patterns": ["cheap hotel"],
    "response": "Budget hotels are available 💸."
},

"luxury_hotel": {
    "patterns": ["luxury hotel"],
    "response": "5-star luxury hotels available ✨."
},

"hotel_price": {
    "patterns": ["hotel price"],
    "response": "Hotel prices depend on date and location 📍."
},

"hotel_amenities": {
    "patterns": ["hotel amenities"],
    "response": "Wi-Fi 📶, breakfast 🍳, AC ❄️ available."
},

"hotel_cancel": {
    "patterns": ["cancel hotel"],
    "response": "Your hotel cancellation ❌🏨 is processed."
},

"hotel_refund": {
    "patterns": ["hotel refund"],
    "response": "Refund depends on hotel policy 💰."
},

"hotel_checkin": {
    "patterns": ["hotel check in"],
    "response": "Standard check-in is after 12 PM ⏰."
},

"hotel_checkout": {
    "patterns": ["hotel checkout"],
    "response": "Standard checkout is before 11 AM ⏰."
},

"hotel_rating": {
    "patterns": ["hotel rating"],
    "response": "We offer 3-star to 5-star hotels ⭐."
},

"nearby_hotel": {
    "patterns": ["nearby hotel"],
    "response": "I can find hotels near your location 📍."
},

"family_hotel": {
    "patterns": ["family hotel"],
    "response": "Family-friendly hotels available 👨‍👩‍👧‍👦."
},

"hotel_support": {
    "patterns": ["hotel help"],
    "response": "Happy to assist with hotel bookings 🏨."
},

# ===================== CABS (66–85) =====================
"book_cab": {
    "patterns": ["book cab"],
    "response": "Cab booking confirmed 🚕."
},

"airport_cab": {
    "patterns": ["airport cab"],
    "response": "Airport pickup/drop available ✈️🚖."
},

"outstation_cab": {
    "patterns": ["outstation cab"],
    "response": "Outstation cab service available 🚗."
},

"local_cab": {
    "patterns": ["local cab"],
    "response": "Local city cab available 🏙️."
},

"cab_price": {
    "patterns": ["cab price"],
    "response": "Cab fare depends on distance 📏."
},

"cab_cancel": {
    "patterns": ["cancel cab"],
    "response": "Your cab cancellation ❌🚕 is processed."
},

"driver_details": {
    "patterns": ["driver details"],
    "response": "Driver details will be shared before pickup 👨‍✈️."
},

"cab_support": {
    "patterns": ["cab help"],
    "response": "I can help with cab booking 🚖."
},

# ===================== PACKAGES (86–105) =====================
"tour_package": {
    "patterns": ["tour package"],
    "response": "We offer exciting tour packages 🌍."
},

"holiday_package": {
    "patterns": ["holiday package"],
    "response": "Perfect holiday packages available 🌴."
},

"honeymoon": {
    "patterns": ["honeymoon"],
    "response": "Romantic honeymoon packages 💕."
},

"family_package": {
    "patterns": ["family package"],
    "response": "Family packages available 👨‍👩‍👧‍👦."
},

"adventure": {
    "patterns": ["adventure trip"],
    "response": "Adventure tours available 🧗."
},

"custom_package": {
    "patterns": ["custom package"],
    "response": "Custom trips designed just for you ✨."
},

"group_trip": {
    "patterns": ["group trip"],
    "response": "Group tour packages available 👥."
},

"package_price": {
    "patterns": ["package price"],
    "response": "Package price depends on itinerary 📋."
},

# ===================== PAYMENTS & SUPPORT (106–120) =====================
"payment": {
    "patterns": ["payment options"],
    "response": "UPI, cards 💳, and net banking accepted."
},

"payment_failed": {
    "patterns": ["payment failed"],
    "response": "Don’t worry 😔 I’ll help resolve it."
},

"refund": {
    "patterns": ["refund"],
    "response": "Refunds are processed in 5–7 days ⏳."
},

"offers": {
    "patterns": ["offers", "discount"],
    "response": "Great offers available 🎉."
},

"booking_status": {
    "patterns": ["booking status"],
    "response": "Please share your booking ID 📄."
},

"customer_support": {
    "patterns": ["customer care"],
    "response": "Our support team is here for you 📞."
},

"complaint": {
    "patterns": ["complaint"],
    "response": "Your complaint has been registered 📝."
},

"feedback": {
    "patterns": ["feedback"],
    "response": "Thanks for your feedback ⭐."
},

"contact": {
    "patterns": ["contact"],
    "response": "📞 9729064340 | 9416074340"
},

"fallback": {
    "patterns": [""],
    "response": "Sorry 🤔 I didn’t understand that. Please try again."
}

}
