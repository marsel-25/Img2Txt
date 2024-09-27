# Img-to-text Application

# Overview
The Img-to-text project is a web application designed to convert images into descriptive text using Google's Generative AI models. It allows users to upload images in various formats and, optionally, input a text prompt that helps the AI model generate more specific content. The application is built with Streamlit, providing a simple, intuitive interface for users to interact with the model.

The AI model used in this application is Google's `gemini-1.5-flash`, which is well-suited for analyzing images and generating text-based content based on those images. Users can either upload an image alone or provide an additional prompt to guide the generation process.

# Features
- Image Upload: Users can upload images in JPG, JPEG, or PNG formats.
- Text Prompt: Optionally, users can provide a text prompt to refine the generated description.
- Image Display: The uploaded image is displayed on the application page.
- AI-generated Text: The application uses Google's AI to generate descriptive text based on the image and prompt.

# How It Works
1. User Input:
   - Users can input a prompt to guide the image-to-text conversion.
   - Users upload an image from their device (supported formats include JPG, JPEG, and PNG).

2. Image Display:
   - The uploaded image is displayed on the app interface for user confirmation.

3. AI Model Processing:
   - The Google Generative AI model (`gemini-1.5-flash`) processes the image and the optional prompt.
   - Based on the provided inputs, the model generates descriptive text or annotations for the image.

4. Response:
   - The generated text is displayed beneath the uploaded image, providing a detailed description or response from the AI.

# Technology Stack
- Streamlit: A Python-based framework for building interactive web applications.
- Pillow: A Python library used to handle image uploads and display.
- Google Generative AI: The core AI used to analyze images and generate text.
- Dotenv: A package used to manage sensitive environment variables such as the API key.

# User Workflow
1. Open the application in a browser.
2. Input an optional text prompt to customize the description of the image.
3. Upload an image in JPG, JPEG, or PNG format.
4. Click the "Submit" button to process the image with Google's AI model.
5. The application returns the generated text based on the image and prompt, which is displayed on the page.

# Purpose
This project provides a simple interface to showcase the potential of AI in generating descriptions or annotations for images. It can be extended to various domains such as content generation, accessibility solutions (e.g., for visually impaired individuals), or even creative tasks like storytelling.

# Future Improvements
- Support for More File Types: Extending the file uploader to accept more image formats.
- Advanced AI Models: Incorporating different or more advanced models for enhanced text generation.
- Customization: Allowing users to adjust settings like the length or style of the generated text.

# Conclusion
The Img-to-text application is a powerful tool that leverages the capabilities of Google's Generative AI to convert images into meaningful text. It is user-friendly, making it accessible for a broad audience to explore AI's potential in image analysis and content generation.

