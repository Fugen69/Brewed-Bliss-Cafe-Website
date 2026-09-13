"""
Brewed Bliss Café — Streamlit Website
A modern, elegant café website built with Streamlit.
"""

import streamlit as st
from menu_data import CATEGORIES, TESTIMONIALS

# ─── Page Configuration ──────────────────────────────────────────────────────

st.set_page_config(
    page_title="Brewed Bliss Café",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ─── Custom CSS ───────────────────────────────────────────────────────────────

def inject_css():
    """Inject custom CSS for a polished cafe aesthetic."""
    st.markdown(
        """
        <style>
        /* ── Import Google Fonts ─────────────────────────── */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Inter:wght@300;400;500;600&display=swap');

        /* ── Root Variables ───────────────────────────────── */
        :root {
            --cafe-brown: #C8A27A;
            --cafe-dark: #1A1A2E;
            --cafe-navy: #16213E;
            --cafe-cream: #E8D5B7;
            --cafe-gold: #D4A55A;
            --cafe-green: #7BC67E;
            --cafe-coral: #E8A87C;
            --cafe-purple: #D4A5FF;
            --font-heading: 'Playfair Display', serif;
            --font-body: 'Inter', sans-serif;
        }

        /* ── Global ──────────────────────────────────────── */
        .stApp {
            font-family: var(--font-body);
        }

        .block-container {
            padding-top: 1rem;
            max-width: 1200px;
        }

        h1, h2, h3 {
            font-family: var(--font-heading) !important;
        }

        /* ── Hero Section ────────────────────────────────── */
        .hero-container {
            text-align: center;
            padding: 4rem 2rem 3rem;
            background: linear-gradient(135deg, #1A1A2E 0%, #16213E 50%, #0F3460 100%);
            border-radius: 20px;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }

        .hero-container::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(200,162,122,0.08) 0%, transparent 50%);
            animation: shimmer 8s ease-in-out infinite;
        }

        @keyframes shimmer {
            0%, 100% { transform: translate(0, 0); }
            50% { transform: translate(30px, 30px); }
        }

        .hero-badge {
            display: inline-block;
            padding: 0.4rem 1.2rem;
            border: 1px solid var(--cafe-brown);
            border-radius: 50px;
            color: var(--cafe-brown);
            font-size: 0.85rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 1.5rem;
            font-family: var(--font-body);
        }

        .hero-title {
            font-family: var(--font-heading);
            font-size: 4rem;
            font-weight: 900;
            color: var(--cafe-cream);
            margin: 0.5rem 0;
            line-height: 1.1;
        }

        .hero-subtitle {
            font-family: var(--font-body);
            font-size: 1.15rem;
            color: #9E9EB8;
            max-width: 600px;
            margin: 1rem auto 2rem;
            line-height: 1.7;
            font-weight: 300;
            text-align: center;
        }

        .hero-emoji {
            font-size: 5rem;
            margin-bottom: 1rem;
            display: block;
        }

        /* ── Section Headers ─────────────────────────────── */
        .section-header {
            text-align: center;
            padding: 2rem 0 1rem;
        }

        .section-header h2 {
            font-family: var(--font-heading);
            font-size: 2.5rem;
            color: var(--cafe-cream);
            margin-bottom: 0.3rem;
        }

        .section-subtitle {
            color: #9E9EB8;
            font-size: 1.05rem;
            font-weight: 300;
        }

        .section-divider {
            width: 60px;
            height: 3px;
            background: var(--cafe-brown);
            margin: 1rem auto;
            border-radius: 2px;
        }

        /* ── Menu Cards ──────────────────────────────────── */
        .menu-card {
            background: linear-gradient(145deg, #16213E, #1A1A2E);
            border: 1px solid rgba(200,162,122,0.15);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .menu-card:hover {
            border-color: rgba(200,162,122,0.4);
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
        }

        .menu-card-emoji {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .menu-card-name {
            font-family: var(--font-heading);
            font-size: 1.25rem;
            color: var(--cafe-cream);
            margin-bottom: 0.3rem;
            font-weight: 600;
        }

        .menu-card-desc {
            color: #9E9EB8;
            font-size: 0.9rem;
            line-height: 1.5;
            margin-bottom: 0.8rem;
            font-weight: 300;
        }

        .menu-card-price {
            font-family: var(--font-heading);
            font-size: 1.4rem;
            color: var(--cafe-brown);
            font-weight: 700;
        }

        .menu-card-rating {
            color: #FFD700;
            font-size: 0.9rem;
        }

        .menu-card-tags {
            margin-top: 0.5rem;
        }

        .tag {
            display: inline-block;
            padding: 0.2rem 0.6rem;
            background: rgba(200,162,122,0.1);
            border: 1px solid rgba(200,162,122,0.2);
            border-radius: 20px;
            color: var(--cafe-brown);
            font-size: 0.75rem;
            margin-right: 0.3rem;
            margin-top: 0.3rem;
        }

        /* ── Category Tabs ───────────────────────────────── */
        .category-card {
            background: linear-gradient(145deg, #16213E, #1A1A2E);
            border: 1px solid rgba(200,162,122,0.15);
            border-radius: 16px;
            padding: 2rem 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .category-card:hover {
            border-color: rgba(200,162,122,0.4);
            transform: translateY(-4px);
            box-shadow: 0 12px 40px rgba(0,0,0,0.3);
        }

        .category-emoji {
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }

        .category-title {
            font-family: var(--font-heading);
            font-size: 1.3rem;
            color: var(--cafe-cream);
            margin-bottom: 0.3rem;
        }

        .category-count {
            color: #9E9EB8;
            font-size: 0.85rem;
        }

        /* ── Testimonial Cards ───────────────────────────── */
        .testimonial-card {
            background: linear-gradient(145deg, #16213E, #1A1A2E);
            border: 1px solid rgba(200,162,122,0.12);
            border-radius: 16px;
            padding: 1.8rem;
            margin-bottom: 1rem;
            position: relative;
        }

        .testimonial-quote {
            font-size: 2rem;
            color: var(--cafe-brown);
            opacity: 0.4;
            position: absolute;
            top: 0.8rem;
            left: 1.2rem;
        }

        .testimonial-text {
            color: #B8B8D0;
            font-size: 0.95rem;
            line-height: 1.7;
            font-style: italic;
            margin-top: 1rem;
            font-weight: 300;
        }

        .testimonial-author {
            color: var(--cafe-cream);
            font-weight: 600;
            margin-top: 1rem;
            font-size: 0.95rem;
        }

        .testimonial-role {
            color: var(--cafe-brown);
            font-size: 0.8rem;
        }

        /* ── Stats Section ───────────────────────────────── */
        .stat-card {
            text-align: center;
            padding: 1.5rem;
        }

        .stat-number {
            font-family: var(--font-heading);
            font-size: 2.5rem;
            font-weight: 900;
            color: var(--cafe-brown);
        }

        .stat-label {
            color: #9E9EB8;
            font-size: 0.9rem;
            font-weight: 300;
            margin-top: 0.3rem;
        }

        /* ── Info Cards (About / Hours) ──────────────────── */
        .info-card {
            background: linear-gradient(145deg, #16213E, #1A1A2E);
            border: 1px solid rgba(200,162,122,0.12);
            border-radius: 16px;
            padding: 2rem;
        }

        .info-card h3 {
            font-family: var(--font-heading);
            color: var(--cafe-cream);
            font-size: 1.4rem;
            margin-bottom: 1rem;
        }

        .info-card p, .info-card li {
            color: #9E9EB8;
            font-size: 0.95rem;
            line-height: 1.7;
            font-weight: 300;
        }

        /* ── Order Summary ───────────────────────────────── */
        .order-item {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid rgba(200,162,122,0.1);
            color: var(--cafe-cream);
            font-size: 0.95rem;
        }

        .order-total {
            display: flex;
            justify-content: space-between;
            padding: 1rem 0 0.5rem;
            color: var(--cafe-brown);
            font-family: var(--font-heading);
            font-size: 1.3rem;
            font-weight: 700;
        }

        /* ── Footer ──────────────────────────────────────── */
        .footer {
            text-align: center;
            padding: 3rem 2rem;
            margin-top: 3rem;
            border-top: 1px solid rgba(200,162,122,0.12);
        }

        .footer-logo {
            font-family: var(--font-heading);
            font-size: 1.5rem;
            color: var(--cafe-cream);
            margin-bottom: 0.5rem;
        }

        .footer-text {
            color: #6B6B80;
            font-size: 0.85rem;
            font-weight: 300;
        }

        .footer-social {
            font-size: 1.5rem;
            margin: 1rem 0;
            letter-spacing: 1rem;
        }

        /* ── Streamlit overrides ─────────────────────────── */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            justify-content: center;
        }

        .stTabs [data-baseweb="tab"] {
            background-color: transparent;
            border: 1px solid rgba(200,162,122,0.2);
            border-radius: 10px;
            padding: 0.5rem 1.5rem;
            color: #9E9EB8;
            font-family: var(--font-body);
        }

        .stTabs [aria-selected="true"] {
            background-color: rgba(200,162,122,0.15) !important;
            border-color: var(--cafe-brown) !important;
            color: var(--cafe-cream) !important;
        }

        div.stButton > button {
            background: linear-gradient(135deg, var(--cafe-brown), var(--cafe-gold));
            color: #1A1A2E;
            font-weight: 600;
            border: none;
            border-radius: 10px;
            padding: 0.5rem 2rem;
            font-family: var(--font-body);
            transition: all 0.3s ease;
        }

        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(200,162,122,0.3);
        }

        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True,
    )


# ─── Helper Functions ────────────────────────────────────────────────────────

def render_stars(rating: float) -> str:
    """Return HTML star string for a given rating."""
    full = int(rating)
    half = 1 if rating - full >= 0.5 else 0
    empty = 5 - full - half
    return "★" * full + ("½" if half else "") + "☆" * empty


def render_hero():
    """Render the hero / landing section."""
    st.markdown(
        """
        <div class="hero-container">
            <span class="hero-emoji">☕</span>
            <div class="hero-badge">Est. 2018 · Artisan Café</div>
            <h1 class="hero-title">Brewed Bliss</h1>
            <p class="hero-subtitle" style="text-align: center !important;">Where every sip tells a story. Discover handcrafted coffees, refreshing beverages, freshly baked short eats, and artisanal ice cream — all under one roof.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stats():
    """Render the stats / highlights bar."""
    cols = st.columns(4)
    stats = [
        ("5,000+", "Happy Customers"),
        ("32", "Menu Items"),
        ("4.8 ★", "Average Rating"),
        ("6", "Years of Brewing"),
    ]
    for col, (number, label) in zip(cols, stats):
        with col:
            st.markdown(
                f"""
                <div class="stat-card">
                    <div class="stat-number">{number}</div>
                    <div class="stat-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_category_overview():
    """Render category cards as a quick overview."""
    st.markdown(
        """
        <div class="section-header">
            <h2>Our Menu</h2>
            <div class="section-divider"></div>
            <p class="section-subtitle">Explore our carefully curated selection</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(4)
    for col, (key, cat) in zip(cols, CATEGORIES.items()):
        with col:
            st.markdown(
                f"""
                <div class="category-card">
                    <div class="category-emoji">{cat['icon']}</div>
                    <div class="category-title">{cat['title'].split(' ', 1)[1]}</div>
                    <div class="category-count">{len(cat['items'])} items</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_menu_section(category_key: str):
    """Render menu items for a given category in a responsive grid."""
    cat = CATEGORIES[category_key]
    st.markdown(
        f"""
        <div class="section-header">
            <h2>{cat['title']}</h2>
            <div class="section-divider"></div>
            <p class="section-subtitle">{cat['subtitle']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(f"<p style='text-align:center; color:#9E9EB8; max-width:700px; margin:0 auto 2rem; font-weight:300;'>{cat['description']}</p>", unsafe_allow_html=True)

    items = cat["items"]
    # Render in rows of 4
    for row_start in range(0, len(items), 4):
        cols = st.columns(4)
        for idx, col in enumerate(cols):
            item_idx = row_start + idx
            if item_idx < len(items):
                item = items[item_idx]
                tags_html = "".join(f'<span class="tag">{t}</span>' for t in item["tags"])
                with col:
                    st.markdown(
                        f"""
                        <div class="menu-card">
                            <div class="menu-card-emoji">{item['image']}</div>
                            <div class="menu-card-name">{item['name']}</div>
                            <div class="menu-card-desc">{item['description']}</div>
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span class="menu-card-price">Rs. {item['price']}</span>
                                <span class="menu-card-rating">{render_stars(item['rating'])} {item['rating']}</span>
                            </div>
                            <div class="menu-card-tags">{tags_html}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )


def render_testimonials():
    """Render customer testimonials."""
    st.markdown(
        """
        <div class="section-header">
            <h2>💬 What Our Customers Say</h2>
            <div class="section-divider"></div>
            <p class="section-subtitle">Real reviews from real coffee lovers</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    for idx, testimonial in enumerate(TESTIMONIALS[:3]):
        with cols[idx % 3]:
            stars = "★" * testimonial["rating"] + "☆" * (5 - testimonial["rating"])
            st.markdown(
                f"""
                <div class="testimonial-card">
                    <div class="testimonial-quote">❝</div>
                    <div class="testimonial-text">{testimonial['text']}</div>
                    <div class="testimonial-author">{testimonial['name']}</div>
                    <div class="testimonial-role">{testimonial['role']}</div>
                    <div style="color: #FFD700; margin-top: 0.5rem;">{stars}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Second row
    cols2 = st.columns([1, 1, 1])
    remaining = TESTIMONIALS[3:5]
    for idx, testimonial in enumerate(remaining):
        with cols2[idx]:
            stars = "★" * testimonial["rating"] + "☆" * (5 - testimonial["rating"])
            st.markdown(
                f"""
                <div class="testimonial-card">
                    <div class="testimonial-quote">❝</div>
                    <div class="testimonial-text">{testimonial['text']}</div>
                    <div class="testimonial-author">{testimonial['name']}</div>
                    <div class="testimonial-role">{testimonial['role']}</div>
                    <div style="color: #FFD700; margin-top: 0.5rem;">{stars}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_order_section():
    """Render the order / cart section."""
    st.markdown(
        """
        <div class="section-header">
            <h2>🛒 Place Your Order</h2>
            <div class="section-divider"></div>
            <p class="section-subtitle">Select items and quantities below</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "cart" not in st.session_state:
        st.session_state.cart = {}

    for cat_key, cat in CATEGORIES.items():
        with st.expander(f"{cat['title']}  —  {len(cat['items'])} items", expanded=False):
            for item in cat["items"]:
                col1, col2, col3 = st.columns([3, 1, 1])
                with col1:
                    st.markdown(f"**{item['image']} {item['name']}**")
                    st.caption(f"Rs. {item['price']}")
                with col2:
                    qty_key = f"qty_{cat_key}_{item['name']}"
                    qty = st.number_input(
                        "Qty",
                        min_value=0,
                        max_value=20,
                        value=st.session_state.cart.get(item["name"], {}).get("qty", 0),
                        key=qty_key,
                        label_visibility="collapsed",
                    )
                    if qty > 0:
                        st.session_state.cart[item["name"]] = {
                            "qty": qty,
                            "price": item["price"],
                            "emoji": item["image"],
                        }
                    elif item["name"] in st.session_state.cart:
                        del st.session_state.cart[item["name"]]
                with col3:
                    if qty > 0:
                        st.markdown(f"**Rs. {item['price'] * qty}**")

    # ── Order Summary ──
    st.markdown("---")
    st.markdown("### 📋 Order Summary")

    cart = st.session_state.cart
    if not cart:
        st.info("Your cart is empty. Add items from the menu above!")
    else:
        total = 0
        for name, details in cart.items():
            if details["qty"] > 0:
                line_total = details["price"] * details["qty"]
                total += line_total
                st.markdown(
                    f"""
                    <div class="order-item">
                        <span>{details['emoji']} {name} × {details['qty']}</span>
                        <span>Rs. {line_total:,}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        import os
        import streamlit.components.v1 as components
        _ts_widget_dir = os.path.join(os.path.dirname(__file__), "ts_widget")
        tip_component = components.declare_component("tip_calculator", path=_ts_widget_dir)
        
        st.markdown("")
        tip_pct = tip_component(default=0, key="tip_calc")
        
        tip_amount = int(total * (tip_pct / 100)) if tip_pct else 0
        final_total = total + tip_amount

        st.markdown(
            f"""
            <div class="order-total" style="font-size: 1rem; color: #9E9EB8;">
                <span>Subtotal</span>
                <span>Rs. {total:,}</span>
            </div>
            <div class="order-total" style="font-size: 1rem; color: #9E9EB8; padding-top: 0;">
                <span>Tip ({tip_pct}%)</span>
                <span>Rs. {tip_amount:,}</span>
            </div>
            <div class="order-total">
                <span>Final Total</span>
                <span>Rs. {final_total:,}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("")
        col_a, col_b, col_c = st.columns([1, 1, 1])
        with col_b:
            if st.button("✨ Confirm Order", use_container_width=True):
                st.balloons()
                st.success(
                    f"🎉 Order placed successfully! Total: **Rs. {final_total:,}**. "
                    "Thank you for choosing Brewed Bliss!"
                )
                st.session_state.cart = {}


def render_about_contact():
    """Render the About & Contact section."""
    st.markdown(
        """
        <div class="section-header">
            <h2>📍 Visit Us</h2>
            <div class="section-divider"></div>
            <p class="section-subtitle">We'd love to welcome you</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="info-card">
                <h3>🏠 About Us</h3>
                <p>
                    Founded in 2018, Brewed Bliss began as a small corner café with a big
                    dream: to serve the perfect cup of coffee. Today, we're proud to offer
                    a full menu of artisan coffees, fresh juices, homemade short eats, and
                    creamy ice cream — all crafted with love and the finest ingredients.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="info-card">
                <h3>🕐 Opening Hours</h3>
                <p>
                    <strong style="color:#E8D5B7;">Monday – Friday</strong><br>
                    7:00 AM – 10:00 PM<br><br>
                    <strong style="color:#E8D5B7;">Saturday – Sunday</strong><br>
                    8:00 AM – 11:00 PM<br><br>
                    <strong style="color:#E8D5B7;">Public Holidays</strong><br>
                    9:00 AM – 9:00 PM
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="info-card">
                <h3>📞 Contact</h3>
                <p>
                    <strong style="color:#E8D5B7;">Address</strong><br>
                    42 Galle Road, Colombo 03<br><br>
                    <strong style="color:#E8D5B7;">Phone</strong><br>
                    +94 11 234 5678<br><br>
                    <strong style="color:#E8D5B7;">Email</strong><br>
                    hello@brewedbliss.lk
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_contact_form():
    """Render a contact / feedback form."""
    st.markdown(
        """
        <div class="section-header">
            <h2>💌 Get In Touch</h2>
            <div class="section-divider"></div>
            <p class="section-subtitle">We'd love to hear from you</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
        with col2:
            phone = st.text_input("Phone Number (optional)")
            subject = st.selectbox(
                "Subject",
                ["General Inquiry", "Feedback", "Catering Request", "Reservation", "Complaint"],
            )
        message = st.text_area("Your Message", height=120)
        submitted = st.form_submit_button("Send Message ✉️", use_container_width=True)
        if submitted:
            if name and email and message:
                st.success(f"Thanks, **{name}**! We've received your message and will get back to you shortly. ☕")
            else:
                st.warning("Please fill in your name, email, and message.")


def render_footer():
    """Render the site footer."""
    st.markdown(
        """
        <div class="footer">
            <div class="footer-social">📷  📘  🐦  📌</div>
            <div class="footer-logo">☕ Brewed Bliss Café</div>
            <div class="footer-text">
                42 Galle Road, Colombo 03 · +94 11 234 5678 · hello@brewedbliss.lk
            </div>
            <div class="footer-text" style="margin-top:0.8rem;">
                © 2026 Brewed Bliss Café. All rights reserved. Crafted with ❤️ and lots of coffee.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ─── Main App ────────────────────────────────────────────────────────────────

def main():
    inject_css()
    render_hero()
    render_stats()

    # Navigation Tabs
    tabs = st.tabs(["🏠 Home", "☕ Coffee", "🥤 Cash Flow", "🥐 Short Eats", "🍨 Ice Cream", "🛒 Order", "📍 About & Contact"])

    with tabs[0]:  # Home
        render_category_overview()
        st.markdown("")
        # Show a "Best Sellers" preview
        st.markdown(
            """
            <div class="section-header">
                <h2>🌟 Best Sellers</h2>
                <div class="section-divider"></div>
                <p class="section-subtitle">Customer favourites you simply must try</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        best_sellers = [
            CATEGORIES["coffee"]["items"][1],      # Cappuccino
            CATEGORIES["cashflow"]["items"][1],     # Mango Smoothie
            CATEGORIES["short_eats"]["items"][3],   # Club Sandwich
            CATEGORIES["ice_cream"]["items"][7],    # Sundae Supreme
        ]
        cols = st.columns(4)
        for col, item in zip(cols, best_sellers):
            tags_html = "".join(f'<span class="tag">{t}</span>' for t in item["tags"])
            with col:
                st.markdown(
                    f"""
                    <div class="menu-card">
                        <div class="menu-card-emoji">{item['image']}</div>
                        <div class="menu-card-name">{item['name']}</div>
                        <div class="menu-card-desc">{item['description']}</div>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="menu-card-price">Rs. {item['price']}</span>
                            <span class="menu-card-rating">{render_stars(item['rating'])} {item['rating']}</span>
                        </div>
                        <div class="menu-card-tags">{tags_html}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        render_testimonials()

    with tabs[1]:  # Coffee
        render_menu_section("coffee")

    with tabs[2]:  # Cash Flow
        render_menu_section("cashflow")

    with tabs[3]:  # Short Eats
        render_menu_section("short_eats")

    with tabs[4]:  # Ice Cream
        render_menu_section("ice_cream")

    with tabs[5]:  # Order
        render_order_section()

    with tabs[6]:  # About & Contact
        render_about_contact()
        st.markdown("")
        render_contact_form()

    render_footer()


if __name__ == "__main__":
    main()
