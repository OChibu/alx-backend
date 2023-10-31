#!/usr/bin/env python3
"""
Module app.py
"""

const userTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;

const currentTime = new Date().toLocaleString('en-US', { timeZone: userTimeZone });

const timeElement = document.getElementById('current-time');
timeElement.innerText = currentTime;

const language = determineUserLanguage(); // Function to determine user's preferred language
const translations = {
  en: 'The current time is %(current_time)s.',
  fr: 'Nous sommes le %(current_time)s.'
};

const translatedMessage = translations[language].replace('%(current_time)s', currentTime);
const messageElement = document.getElementById('message');
messageElement.innerText = translatedMessage;
