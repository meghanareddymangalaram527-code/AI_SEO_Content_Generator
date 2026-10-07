import streamlit as st
from seo_generator import SEOContentGenerator


# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI SEO Content Generator",
    page_icon="🔍",
    layout="wide"
)


# ---------------------------------------------------------
# CREATE SEO GENERATOR
# ---------------------------------------------------------

generator = SEOContentGenerator()


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("🔍 AI SEO Content Generator")

st.write(
    "Generate SEO-optimized content using Python and NLP."
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.header("⚙️ Content Settings")

topic = st.sidebar.text_input(
    "Enter your topic / keyword",
    value="Machine Learning"
)

generate_button = st.sidebar.button(
    "🚀 Generate SEO Content"
)


# ---------------------------------------------------------
# GENERATE CONTENT
# ---------------------------------------------------------

if generate_button:

    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic or keyword.")

    else:

        with st.spinner("Generating SEO content..."):

            # Generate SEO content
            result = generator.generate_content(topic)

            title = result["title"]

            meta_description = result["meta_description"]

            keywords = result["keywords"]

            headings = result["headings"]

            content = result["content"]


            # Calculate keyword density
            keyword_density = generator.calculate_keyword_density(
                content,
                topic
            )


            # Calculate readability
            readability = generator.calculate_readability(
                content
            )


            # Calculate word count
            word_count = len(content.split())


            # Calculate overall SEO score
            seo_score = generator.calculate_seo_score(
                title,
                meta_description,
                keyword_density,
                readability,
                word_count
            )


        # -------------------------------------------------
        # SUCCESS MESSAGE
        # -------------------------------------------------

        st.success(
            "✅ SEO content generated successfully!"
        )


        # -------------------------------------------------
        # OVERALL SEO SCORE
        # -------------------------------------------------

        st.header("🎯 Overall SEO Score")

        st.metric(
            label="SEO Score",
            value=f"{seo_score}/100"
        )


        if seo_score >= 80:

            st.success(
                "🟢 Excellent SEO score!"
            )

        elif seo_score >= 60:

            st.info(
                "🟡 Good SEO score. Some improvements are possible."
            )

        else:

            st.warning(
                "🟠 SEO score can be improved."
            )


        # -------------------------------------------------
        # SEO TITLE
        # -------------------------------------------------

        st.header("📌 SEO Title")

        st.write(title)

        st.caption(
            f"Title length: {len(title)} characters"
        )


        # -------------------------------------------------
        # META DESCRIPTION
        # -------------------------------------------------

        st.header("📄 Meta Description")

        st.write(meta_description)

        st.caption(
            f"Meta description length: "
            f"{len(meta_description)} characters"
        )


        # -------------------------------------------------
        # KEYWORDS
        # -------------------------------------------------

        st.header("🏷️ Keywords")

        st.write(
            ", ".join(keywords)
        )


        # -------------------------------------------------
        # HEADING STRUCTURE
        # -------------------------------------------------

        st.header("📑 Heading Structure")


        st.subheader("H1")

        st.write(
            headings["H1"]
        )


        st.subheader("H2")

        for heading in headings["H2"]:

            st.write(
                f"• {heading}"
            )


        st.subheader("H3")

        for heading in headings["H3"]:

            st.write(
                f"• {heading}"
            )


        # -------------------------------------------------
        # SEO ANALYSIS
        # -------------------------------------------------

        st.header("📊 SEO Analysis")

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Keyword Density",
                f"{keyword_density}%"
            )


        with col2:

            st.metric(
                "Readability",
                f"{readability}/100"
            )


        with col3:

            st.metric(
                "Word Count",
                word_count
            )


        # -------------------------------------------------
        # SEO CHECKS
        # -------------------------------------------------

        st.header("✅ SEO Checks")


        # Title check
        if 40 <= len(title) <= 60:

            st.success(
                "✅ SEO title length is good."
            )

        else:

            st.warning(
                "⚠️ SEO title length can be improved."
            )


        # Meta description check
        if 120 <= len(meta_description) <= 160:

            st.success(
                "✅ Meta description length is good."
            )

        else:

            st.warning(
                "⚠️ Meta description length can be improved."
            )


        # Keyword density check
        if 0.5 <= keyword_density <= 2.5:

            st.success(
                "✅ Keyword density is within the recommended range."
            )

        else:

            st.warning(
                "⚠️ Keyword density can be improved."
            )


        # Readability check
        if readability >= 60:

            st.success(
                "✅ Content readability is good."
            )

        else:

            st.warning(
                "⚠️ Content readability can be improved."
            )


        # Word count check
        if word_count >= 300:

            st.success(
                "✅ Content has a good word count."
            )

        else:

            st.warning(
                "⚠️ Content word count can be increased."
            )


        # -------------------------------------------------
        # GENERATED CONTENT
        # -------------------------------------------------

        st.header("📝 Generated Content")

        st.markdown(content)


        # -------------------------------------------------
        # DOWNLOAD
        # -------------------------------------------------

        st.header("📥 Download Content")

        st.download_button(
            label="📥 Download SEO Content",
            data=content,
            file_name="seo_content.txt",
            mime="text/plain"
        )


# ---------------------------------------------------------
# INITIAL SCREEN
# ---------------------------------------------------------

else:

    st.info(
        "👈 Enter a topic or keyword in the sidebar "
        "and click Generate SEO Content."
    )


    st.header("✨ Features")

    st.markdown("""
    - 🔍 Keyword Research & Generation
    - 📌 SEO Title Generation
    - 📄 Meta Description Generation
    - 📑 Heading Structure
    - ✍️ Content Generation
    - 📊 Keyword Density Analysis
    - 📖 Readability Analysis
    - 🎯 Overall SEO Score
    - ✅ SEO Quality Checks
    - 📥 Content Download
    """)
