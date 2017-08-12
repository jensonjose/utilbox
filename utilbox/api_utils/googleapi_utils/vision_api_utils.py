"""
Utility module for interaction with the Google Vision API.

Usage requires a Google Cloud Platform account with a valid API key.

Most of this code has been adapted from the Google Cloud Platform sample code available here:
https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/vision/cloud-client/detect/detect.py

The sample code from the above link is under the Apache 2.0 license. Link to the license text:
http://www.apache.org/licenses/LICENSE-2.0
"""

import io
from google.cloud import vision
from google.cloud.vision import types


class VisionApiUtils:
    """
    Class containing methods for interaction with the Google Vision API.
    """

    def __init__(self):
        pass

    @staticmethod
    def detect_faces(path):
        """Detects faces in an image."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.face_detection(image=image)
        faces = response.face_annotations

        # Names of likelihood from google.cloud.vision.enums
        likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                           'LIKELY', 'VERY_LIKELY')
        print('Faces:')

        for face in faces:
            print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
            print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
            print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in face.bounding_poly.vertices])

            print('face bounds: {}'.format(','.join(vertices)))

    @staticmethod
    def detect_faces_uri(uri):
        """Detects faces in the file located in Google Cloud Storage or the web."""
        client = vision.ImageAnnotatorClient()

        image = types.Image()
        image.source.image_uri = uri

        response = client.face_detection(image=image)
        faces = response.face_annotations

        # Names of likelihood from google.cloud.vision.enums
        likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                           'LIKELY', 'VERY_LIKELY')
        print('Faces:')

        for face in faces:
            print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
            print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
            print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in face.bounding_poly.vertices])

            print('face bounds: {}'.format(','.join(vertices)))

    @staticmethod
    def detect_labels(path):
        """Detects labels in the file."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.label_detection(image=image)
        labels = response.label_annotations
        print('Labels:')

        for label in labels:
            print(label.description)

    @staticmethod
    def detect_labels_uri(uri):
        """Detects labels in the file located in Google Cloud Storage or on the
        Web."""
        client = vision.ImageAnnotatorClient()
        image = types.Image()
        image.source.image_uri = uri

        response = client.label_detection(image=image)
        labels = response.label_annotations
        print('Labels:')

        for label in labels:
            print(label.description)

    @staticmethod
    def detect_landmarks(path):
        """Detects landmarks in the file."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.landmark_detection(image=image)
        landmarks = response.landmark_annotations
        print('Landmarks:')

        for landmark in landmarks:
            print(landmark.description)
            for location in landmark.locations:
                lat_lng = location.lat_lng
                print('Latitude'.format(lat_lng.latitude))
                print('Longitude'.format(lat_lng.longitude))

    @staticmethod
    def detect_landmarks_uri(uri):
        """Detects landmarks in the file located in Google Cloud Storage or on the
        Web."""
        client = vision.ImageAnnotatorClient()
        image = types.Image()
        image.source.image_uri = uri

        response = client.landmark_detection(image=image)
        landmarks = response.landmark_annotations
        print('Landmarks:')

        for landmark in landmarks:
            print(landmark.description)

    @staticmethod
    def detect_logos(path):
        """Detects logos in the file."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.logo_detection(image=image)
        logos = response.logo_annotations
        print('Logos:')

        for logo in logos:
            print(logo.description)

    @staticmethod
    def detect_logos_uri(uri):
        """Detects logos in the file located in Google Cloud Storage or on the Web.
        """
        client = vision.ImageAnnotatorClient()
        image = types.Image()
        image.source.image_uri = uri

        response = client.logo_detection(image=image)
        logos = response.logo_annotations
        print('Logos:')

        for logo in logos:
            print(logo.description)

    @staticmethod
    def detect_safe_search(path):
        """Detects unsafe features in the file."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.safe_search_detection(image=image)
        safe = response.safe_search_annotation

        # Names of likelihood from google.cloud.vision.enums
        likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                           'LIKELY', 'VERY_LIKELY')
        print('Safe search:')

        print('adult: {}'.format(likelihood_name[safe.adult]))
        print('medical: {}'.format(likelihood_name[safe.medical]))
        print('spoofed: {}'.format(likelihood_name[safe.spoof]))
        print('violence: {}'.format(likelihood_name[safe.violence]))

    @staticmethod
    def detect_safe_search_uri(uri):
        """Detects unsafe features in the file located in Google Cloud Storage or
        on the Web."""
        client = vision.ImageAnnotatorClient()
        image = types.Image()
        image.source.image_uri = uri

        response = client.safe_search_detection(image=image)
        safe = response.safe_search_annotation

        # Names of likelihood from google.cloud.vision.enums
        likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                           'LIKELY', 'VERY_LIKELY')
        print('Safe search:')

        print('adult: {}'.format(likelihood_name[safe.adult]))
        print('medical: {}'.format(likelihood_name[safe.medical]))
        print('spoofed: {}'.format(likelihood_name[safe.spoof]))
        print('violence: {}'.format(likelihood_name[safe.violence]))

    @staticmethod
    def detect_text(path):
        """Detects text in the file."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')

        for text in texts:
            print('\n"{}"'.format(text.description))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in text.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))

    @staticmethod
    def detect_text_uri(uri):
        """Detects text in the file located in Google Cloud Storage or on the Web.
        """
        client = vision.ImageAnnotatorClient()
        image = types.Image()
        image.source.image_uri = uri

        response = client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')

        for text in texts:
            print('\n"{}"'.format(text.description))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in text.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))

    @staticmethod
    def detect_text_full(path):
        """Detects text in the file and returns the full transcript."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
        response = client.text_detection(image=image)

        if len(response.text_annotations) > 0:
            return response.text_annotations[0].description.encode("utf-8")

        return False

    @staticmethod
    def detect_properties(path):
        """Detects image properties in the file."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.image_properties(image=image)
        props = response.image_properties_annotation
        print('Properties:')

        for color in props.dominant_colors.colors:
            print('fraction: {}'.format(color.pixel_fraction))
            print('\tr: {}'.format(color.color.red))
            print('\tg: {}'.format(color.color.green))
            print('\tb: {}'.format(color.color.blue))
            print('\ta: {}'.format(color.color.alpha))

    @staticmethod
    def detect_properties_uri(uri):
        """Detects image properties in the file located in Google Cloud Storage or
        on the Web."""
        client = vision.ImageAnnotatorClient()
        image = types.Image()
        image.source.image_uri = uri

        response = client.image_properties(image=image)
        props = response.image_properties_annotation
        print('Properties:')

        for color in props.dominant_colors.colors:
            print('frac: {}'.format(color.pixel_fraction))
            print('\tr: {}'.format(color.color.red))
            print('\tg: {}'.format(color.color.green))
            print('\tb: {}'.format(color.color.blue))
            print('\ta: {}'.format(color.color.alpha))

    @staticmethod
    def detect_web(path):
        """Detects web annotations given an image."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.web_detection(image=image)
        notes = response.web_detection

        if notes.pages_with_matching_images:
            print('\n{} Pages with matching images retrieved')

            for page in notes.pages_with_matching_images:
                print('Url   : {}'.format(page.url))

        if notes.full_matching_images:
            print ('\n{} Full Matches found: '.format(
                   len(notes.full_matching_images)))

            for image in notes.full_matching_images:
                print('Url  : {}'.format(image.url))

        if notes.partial_matching_images:
            print ('\n{} Partial Matches found: '.format(
                   len(notes.partial_matching_images)))

            for image in notes.partial_matching_images:
                print('Url  : {}'.format(image.url))

        if notes.web_entities:
            print ('\n{} Web entities found: '.format(len(notes.web_entities)))

            for entity in notes.web_entities:
                print('Score      : {}'.format(entity.score))
                print('Description: {}'.format(entity.description))

    @staticmethod
    def detect_web_uri(uri):
        """Detects web annotations in the file located in Google Cloud Storage."""
        client = vision.ImageAnnotatorClient()
        image = types.Image()
        image.source.image_uri = uri

        response = client.web_detection(image=image)
        notes = response.web_detection

        if notes.pages_with_matching_images:
            print('\n{} Pages with matching images retrieved')

            for page in notes.pages_with_matching_images:
                print('Url   : {}'.format(page.url))

        if notes.full_matching_images:
            print ('\n{} Full Matches found: '.format(
                   len(notes.full_matching_images)))

            for image in notes.full_matching_images:
                print('Url  : {}'.format(image.url))

        if notes.partial_matching_images:
            print ('\n{} Partial Matches found: '.format(
                   len(notes.partial_matching_images)))

            for image in notes.partial_matching_images:
                print('Url  : {}'.format(image.url))

        if notes.web_entities:
            print ('\n{} Web entities found: '.format(len(notes.web_entities)))

            for entity in notes.web_entities:
                print('Score      : {}'.format(entity.score))
                print('Description: {}'.format(entity.description))

    @staticmethod
    def detect_crop_hints(path):
        """Detects crop hints in an image."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)

        crop_hints_params = types.CropHintsParams(aspect_ratios=[1.77])
        image_context = types.ImageContext(crop_hints_params=crop_hints_params)

        response = client.crop_hints(image=image, image_context=image_context)
        hints = response.crop_hints_annotation.crop_hints

        for n, hint in enumerate(hints):
            print('\nCrop Hint: {}'.format(n))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in hint.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))

    @staticmethod
    def detect_crop_hints_uri(uri):
        """Detects crop hints in the file located in Google Cloud Storage."""
        client = vision.ImageAnnotatorClient()
        image = types.Image()
        image.source.image_uri = uri

        crop_hints_params = types.CropHintsParams(aspect_ratios=[1.77])
        image_context = types.ImageContext(crop_hints_params=crop_hints_params)

        response = client.crop_hints(image=image, image_context=image_context)
        hints = response.crop_hints_annotation.crop_hints

        for n, hint in enumerate(hints):
            print('\nCrop Hint: {}'.format(n))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in hint.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))

    @staticmethod
    def detect_document(path):
        """Detects document features in an image."""
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.document_text_detection(image=image)
        document = response.full_text_annotation

        for page in document.pages:
            for block in page.blocks:
                block_words = []
                for paragraph in block.paragraphs:
                    block_words.extend(paragraph.words)

                block_symbols = []
                for word in block_words:
                    block_symbols.extend(word.symbols)

                block_text = ''
                for symbol in block_symbols:
                    block_text = block_text + symbol.text

                print('Block Content: {}'.format(block_text))
                print('Block Bounds:\n {}'.format(block.bounding_box))

    @staticmethod
    def detect_document_uri(uri):
        """Detects document features in the file located in Google Cloud
        Storage."""
        client = vision.ImageAnnotatorClient()
        image = types.Image()
        image.source.image_uri = uri

        response = client.document_text_detection(image=image)
        document = response.full_text_annotation

        for page in document.pages:
            for block in page.blocks:
                block_words = []
                for paragraph in block.paragraphs:
                    block_words.extend(paragraph.words)

                block_symbols = []
                for word in block_words:
                    block_symbols.extend(word.symbols)

                block_text = ''
                for symbol in block_symbols:
                    block_text = block_text + symbol.text

                print('Block Content: {}'.format(block_text))
                print('Block Bounds:\n {}'.format(block.bounding_box))
