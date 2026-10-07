
import random
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Download required NLTK data
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)


class SEOContentGenerator:

    def __init__(self):
        self.stop_words = set(stopwords.words("english"))

        self.primary_modifiers = [
            "best",
            "top",
            "ultimate",
            "complete",
            "essential",
            "professional",
            "beginner"
        ]

        self.secondary_modifiers = [
            "guide",
            "tutorial",
            "tips",
            "strategies",
            "best practices",
            "tools"
        ]

        self.lsi_keywords = [
            "learning",
            "training",
            "skills",
            "knowledge",
            "practice",
            "development",
            "growth",
            "success"
        ]

    def generate_keywords(self, topic):
        topic = topic.lower().strip()

        keywords = [topic]

        for modifier in self.primary_modifiers:
            keywords.append(f"{modifier} {topic}")

        for modifier in self.secondary_modifiers:
            keywords.append(f"{topic} {modifier}")

        keywords.extend(self.lsi_keywords)

        return list(dict.fromkeys(keywords))

    def generate_title(self, keyword):
        titles = [
            f"The Complete Guide to {keyword.title()}",
            f"Best {keyword.title()} Guide: Tips and Strategies",
            f"How to Master {keyword.title()}: Complete Guide",
            f"{keyword.title()}: Ultimate Guide for Beginners",
            f"Complete {keyword.title()} Guide and Best Practices"
        ]

        suitable_titles = [
            title for title in titles
            if 40 <= len(title) <= 60
        ]

        if suitable_titles:
            return random.choice(suitable_titles)

        title = titles[0]

        if len(title) > 60:
            title = title[:57] + "..."

        return title

    def generate_meta_description(self, keyword):
        descriptions = [
            f"Learn {keyword} with this complete guide covering essential concepts, practical techniques, useful tools, expert tips, and effective strategies.",
            f"Discover {keyword} with practical tips, useful tools, proven strategies, important benefits, and best practices for achieving better results.",
            f"Explore {keyword} through this comprehensive guide covering key concepts, techniques, tools, benefits, tips, and useful best practices."
        ]

        suitable_descriptions = [
            description
            for description in descriptions
            if 120 <= len(description) <= 160
        ]

        if suitable_descriptions:
            return random.choice(suitable_descriptions)

        description = descriptions[0]

        if len(description) > 160:
            description = description[:157] + "..."

        return description

    def generate_headings(self, keyword):
        return {
            "H1": self.generate_title(keyword),

            "H2": [
                f"What is {keyword.title()}?",
                f"Key Benefits of {keyword.title()}",
                f"How to Get Started with {keyword.title()}",
                f"Best Tips for {keyword.title()}",
                f"Common Mistakes in {keyword.title()}",
                "Conclusion"
            ],

            "H3": [
                f"Understanding {keyword.title()}",
                f"Important {keyword.title()} Techniques",
                f"Tools and Resources for {keyword.title()}"
            ]
        }

    def generate_content(self, keyword):

        title = self.generate_title(keyword)
        meta = self.generate_meta_description(keyword)
        keywords = self.generate_keywords(keyword)
        headings = self.generate_headings(keyword)

        content = f"""
# {title}

## Introduction

{keyword.title()} is an important topic in today's digital world.
Learning {keyword} can help students, professionals, and businesses
develop useful knowledge and practical skills.

This guide explains {keyword} in a simple and structured way.
It covers important concepts, benefits, techniques, tools,
and best practices.

## What is {keyword.title()}?

{keyword.title()} refers to the concepts, techniques, methods,
and practices associated with {keyword}.

Understanding {keyword} requires learning the basic concepts,
practicing important techniques, and applying knowledge to
real-world situations.

## Key Benefits of {keyword.title()}

The important benefits of {keyword} include:

- Improved knowledge and skills
- Better productivity
- Increased efficiency
- Professional development
- Better decision making
- Improved problem solving
- Career growth opportunities

## How to Get Started with {keyword.title()}

Follow these steps to learn {keyword}:

1. Learn the basic concepts.
2. Understand important terminology.
3. Study current trends.
4. Practice regularly.
5. Use useful tools and resources.
6. Work on practical examples.
7. Analyze your results.
8. Continue improving your skills.

## Best Tips for {keyword.title()}

Start with the fundamentals of {keyword} before learning
advanced concepts.

Practice consistently and use reliable learning resources.
Stay updated with current developments and industry trends.

Apply your knowledge through practical projects.
This helps improve understanding and develops useful skills.

## Common Mistakes in {keyword.title()}

Avoid these common mistakes:

- Using irrelevant keywords
- Repeating keywords excessively
- Using unclear headings
- Writing very long sentences
- Ignoring readability
- Creating poorly structured content
- Using an unsuitable title

## Tools and Resources

Useful tools and resources can make learning {keyword} easier.
Choose resources based on your objectives and use them regularly.

Practical examples, tutorials, documentation, and projects can
help improve your understanding and experience.

## Conclusion

{keyword.title()} provides valuable opportunities for learning,
skill development, productivity, and professional growth.

By learning the fundamentals, practicing regularly, using useful
tools, and following good content practices, you can achieve
better results with {keyword}.
"""

        return {
            "title": title,
            "meta_description": meta,
            "keywords": keywords,
            "headings": headings,
            "content": content
        }

    def calculate_keyword_density(self, content, keyword):
        words = content.lower().split()

        if not words:
            return 0

        keyword_count = content.lower().count(keyword.lower())

        density = (keyword_count / len(words)) * 100

        return round(density, 2)

    def calculate_readability(self, content):

        clean_content = re.sub(r"[#*_]", "", content)

        sentences = sent_tokenize(clean_content)
        words = word_tokenize(clean_content)

        words = [
            word for word in words
            if word.isalpha()
        ]

        if not sentences or not words:
            return 0

        average_sentence_length = len(words) / len(sentences)

        score = 100 - (average_sentence_length * 1.2)

        score = max(0, min(100, score))

        return round(score, 2)

    def calculate_seo_score(
        self,
        title,
        meta_description,
        keyword_density,
        readability,
        word_count
    ):
        score = 0

        # Title: 25 points
        if 50 <= len(title) <= 60:
            score += 25
        elif 40 <= len(title) <= 70:
            score += 20
        else:
            score += 10

        # Meta description: 25 points
        if 150 <= len(meta_description) <= 160:
            score += 25
        elif 120 <= len(meta_description) <= 170:
            score += 20
        else:
            score += 10

        # Keyword density: 20 points
        if 0.5 <= keyword_density <= 2.5:
            score += 20
        elif 0.2 <= keyword_density <= 3.0:
            score += 15
        else:
            score += 5

        # Readability: 15 points
        if readability >= 60:
            score += 15
        elif readability >= 40:
            score += 10
        else:
            score += 5

        # Word count: 15 points
        if word_count >= 500:
            score += 15
        elif word_count >= 300:
            score += 10
        elif word_count >= 150:
            score += 5

        return min(score, 100)
