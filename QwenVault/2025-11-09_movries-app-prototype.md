---
title: "Movries App Prototype"
date: 2025-11-09
tags:
  - sql
  - machine-learning
  - linux
  - stock-market
  - projects
  - web-dev
  - game-design
source: qwen-export
model: qwen3-max-2025-10-20
---

# Movries App Prototype

**Date:** 2025-11-09  
**Model:** `qwen3-max-2025-10-20`  
**Topics:** [[SQL]] · [[Machine-Learning]] · [[Linux]] · [[Stock-Market]] · [[Projects]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

Of course. As a senior frontend engineer, I'll provide you with a comprehensive, professional-grade prompt that would be used to architect and build the "Movries" application from the ground up. I will then detail the technologies and patterns employed.
The Development Prompt & Specification
Here is the complete prompt to build the "Movries" application. This specification is designed to be given to an advanced AI developer or a senior engineering team.
Project Goal:
Build "Movries," a modern, responsive, and aesthetically pleasing Progressive Web App (PWA) for users to track their favorite movies and TV series. The application's standout feature will be its deep integration with the Google Gemini API to provide AI-powered search, content autofill, and image generation capabilities. The entire application will be a single-page app built with React and TypeScript.
Core Technologies:
Framework: React (using modern hooks)
Language: TypeScript
Styling: Tailwind CSS (configured directly in the HTML for simplicity)
AI: Google Gemini API via the @google/genai SDK
Data Persistence: Browser localStorage
Detailed Feature Requirements:
1. Data Model & Core Logic (types.ts, hooks/useMediaLibrary.ts)
MediaItem Type: Define an interface for a media item containing: id (string), title (string), year (number), type ('movie' | 'series'), rating (number, 0-10), genre (optional string), poster (string URL or data URI), createdAt (ISO string), and plot (optional string, used transiently for AI poster generation).
useMediaLibrary Hook: Create a custom hook to manage the collection of MediaItems.
It must initialize its state from localStorage on mount.
It must persist any changes back to localStorage.
It must expose functions for addItem, updateItem, and deleteItem.
It must include an exportLibrary function that stringifies the media list and triggers a browser download of the resulting JSON file.
2. Gemini API Service (services/geminiService.ts)
Encapsulate all Gemini API interactions within this service file. Initialize a single GoogleGenAI client instance.
getMediaDetails (Autofill):
Purpose: Given a title string, fetch detailed information.
Model: gemini-2.5-pro.
Implementation: Use ai.models.generateContent with responseMimeType: 'application/json'.
Schema: Provide a strict responseSchema to enforce a JSON object output containing title, year, type ('movie' or 'series'), rating, genre, poster (public domain URL), and plot (one-sentence summary).
Error Handling: Throw an error if the response structure is invalid.
searchMedia (AI Search):
Purpose: Given a natural language query, find up to 5 matching movies or series.
Model: gemini-2.5-pro.
Implementation: Use ai.models.generateContent with responseMimeType: 'application/json'.
Schema: Provide a schema that returns an object with a single key, results, which is an array of media items. Each item in the array should contain title, year, type, rating, genre, and poster.
generatePosterFromDetails (AI Poster Generation):
Purpose: Create a new, artistic poster based on item details.
Model: gemini-2.5-flash-image.
Prompt: Construct a detailed prompt asking for a "visually striking, artistic movie poster" for the given title, year, and genre, based on the plot. Crucially, instruct the model not to include any text.
Implementation: Use ai.models.generateContent with config: { responseModalities: [Modality.IMAGE] }.
Output: Extract the base64 image data from the response and return it as a data URI (data:image/png;base64,...).
editImageWithPrompt (AI Poster Editing):
Purpose: Modify an existing image using a text prompt.
Model: gemini-2.5-flash-image.
Implementation: Use ai.models.generateContent, providing two parts in the contents: the original image as inlineData (base64 string and mimeType) and the user's text prompt. Set config: { responseModalities: [Modality.IMAGE] }.
Output: Return the modified image as a data URI.
3. UI Components (components/)
Build a modular and reusable component library.
App.tsx (Main Component):
Orchestrate all state and components.
Manage the open/closed state for all modals.
Handle toast notifications.
Header.tsx: A simple header with the app title "MOVRIES", an "Export" button, and an "Add Item" button.
ImdbSearchBar.tsx:
The primary AI search interface.
Use a custom useImdbSearch hook to manage search state (loading, results).
On submit, call the searchMedia service function.
Display results in a dropdown list below the search bar. Each result should show the poster, title, year, rating, and an "Add" button to directly add it to the library.
FilterTabs.tsx: Tabs for "All", "Movies", and "TV Series" to filter the main grid view.
MediaGrid.tsx & MediaCard.tsx:
The grid should responsively display MediaCard components. Show a message if the library is empty.
The card must display the poster, title, year, type, and rating.
On hover, the card should have a subtle lift effect (transform: -translate-y-1) and reveal controls:
A "Delete" button (TrashIcon).
An "Edit Poster" button (PhotoIcon).
An IMDb search link (ExternalLinkIcon).
Clicking the card itself should open the AddEditModal for editing.
AddEditModal.tsx:
A comprehensive form for adding or editing a MediaItem.
Include a title input with an attached "Autofill" button (SparklesIcon) that triggers getMediaDetails.
Include inputs for all other MediaItem fields.
Show a poster preview. Next to it, include an "Generate AI Poster" button (PhotoIcon) that triggers generatePosterFromDetails. This button should be disabled until the details have been autofilled (to ensure a plot is available).
ImageEditModal.tsx:
Displays the current poster.
Provides a text input for an editing prompt (e.g., "make it black and white").
A "Generate" button calls editImageWithPrompt and updates the displayed image with the result.
A "Save" button commits the new image URL.
Other Modals & UI: ConfirmDeleteModal.tsx for deletions and Toast.tsx for non-blocking feedback.
4. Styling and UX:
Theme: Use a dark, modern theme with a specific color palette:
Background: #111827
Surface: #1F2937
Borders: #374151
Primary Accent: #FBBF24 (Amber/Gold)
Danger: #EF4444 (Red)
Responsiveness: Ensure the layout, especially the MediaGrid, adapts gracefully from mobile to desktop screens.
Feedback: All asynchronous actions (API calls) must have clear loading states (e.g., button text changes to "...", disabled states).
Transitions: Use smooth CSS transitions for hover effects and modal appearances to create a polished feel.
Technologies & Concepts Used
Here is a summary of everything used to build this application, as a senior developer would describe it:
Frontend Framework & Language:
React: The application is built on React, leveraging functional components and the full suite of Hooks (useState, useEffect, useMemo, useCallback) for state and lifecycle management.
TypeScript: Used for static typing to ensure code quality, maintainability, and catch errors early. It provides type safety for component props, state, and API service responses.
AI Integration:
Google Gemini API (@google/genai): This is the core of the AI functionality.
gemini-2.5-pro: Chosen for advanced reasoning tasks like interpreting natural language search queries and structuring detailed information into a guaranteed JSON format. Its strength is in complex text-to-text generation.
gemini-2.5-flash-image: A specialized and efficient model used for all visual tasks—both generating a poster from a descriptive prompt and editing an existing image based on instructions.
JSON Mode: We explicitly force JSON output from the model using responseMimeType and responseSchema. This is a professional pattern that eliminates unreliable string parsing and provides predictable, structured data.
Multimodality: The app uses both text-only and multimodal (text + image) inputs to the Gemini models, showcasing a key feature of the API.
Architecture & Design Patterns:
Component-Based Architecture: The UI is broken down into small, reusable, and self-contained components (e.g., MediaCard, FilterTabs), which is a fundamental React pattern.
Separation of Concerns: The code is logically organized:
components/: All UI-related code.
hooks/: Reusable stateful logic (business logic) is extracted into custom hooks, cleaning up components.
services/: All external API communication is isolated in a service layer, making the app easier to test and maintain.
types/: A single source of truth for all data structures.
State Management: Local component state is managed with useState. For more complex, cross-component logic, custom hooks (useMediaLibrary, useImdbSearch) act as localized state managers.
Styling:
Tailwind CSS: A utility-first CSS framework is used for rapid, consistent, and maintainable styling directly within the JSX. The theme is customized with a specific, modern dark-mode color palette.
Browser APIs & Data Handling:
localStorage: Used for simple, client-side data persistence, making the user's library survive page reloads.
Fetch API & FileReader: Used in combination within the imageUtils.ts file to programmatically fetch an image from a URL (bypassing potential CORS issues in some scenarios) and convert it into the base64 format required by the Gemini API.
File Export: Standard web APIs (Blob, URL.createObjectURL) are used to generate and trigger the download of the JSON library export.

---
