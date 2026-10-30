-- Amazon US & Germany Product Intelligence Database Schema
-- Compatible with SQLite 3 and PostgreSQL 14+

-- 1. Marketplaces Table
CREATE TABLE IF NOT EXISTS marketplaces (
    marketplace_id VARCHAR(10) PRIMARY KEY, -- e.g., 'US', 'DE'
    country_name VARCHAR(50) NOT NULL,
    domain VARCHAR(50) NOT NULL,           -- 'amazon.com', 'amazon.de'
    currency VARCHAR(5) NOT NULL,          -- 'USD', 'EUR'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Categories Table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    marketplace_id VARCHAR(10) NOT NULL,
    category_name VARCHAR(100) NOT NULL,
    amazon_browse_node VARCHAR(50),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (marketplace_id) REFERENCES marketplaces(marketplace_id)
);

-- 3. Products Catalog Table
CREATE TABLE IF NOT EXISTS products (
    asin VARCHAR(20) NOT NULL,
    marketplace_id VARCHAR(10) NOT NULL,
    title TEXT NOT NULL,
    brand VARCHAR(100),
    product_url TEXT NOT NULL,
    main_image_url TEXT,
    category_id INTEGER,
    launch_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (asin, marketplace_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (marketplace_id) REFERENCES marketplaces(marketplace_id)
);

-- 4. Weekly Snapshots Table (Top 50 Tracking by Week)
CREATE TABLE IF NOT EXISTS weekly_snapshots (
    snapshot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    asin VARCHAR(20) NOT NULL,
    marketplace_id VARCHAR(10) NOT NULL,
    category_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    week_number INTEGER NOT NULL,
    snapshot_date DATE NOT NULL,
    
    -- Performance Metrics
    bsr_rank INTEGER NOT NULL,              -- Best Sellers Rank (1 - 50)
    price DECIMAL(10, 2) NOT NULL,
    rating DECIMAL(3, 2),                  -- e.g., 4.6
    review_count INTEGER,
    est_monthly_sales INTEGER,             -- Algorithmic estimate
    est_monthly_revenue DECIMAL(12, 2),
    
    -- Velocity Flags
    is_hot_new_release BOOLEAN DEFAULT 0,
    is_mover_shaker BOOLEAN DEFAULT 0,
    bsr_change_7d INTEGER DEFAULT 0,       -- Positive = rank improved
    review_growth_rate_pct DECIMAL(5, 2),  -- Review velocity
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (asin, marketplace_id) REFERENCES products(asin, marketplace_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- 5. Product Development Evaluation & Opportunity Scoring Table
CREATE TABLE IF NOT EXISTS product_opportunities (
    opportunity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    asin VARCHAR(20) NOT NULL,
    marketplace_id VARCHAR(10) NOT NULL,
    snapshot_id INTEGER NOT NULL,
    
    -- Scoring Metrics (0 to 100)
    opportunity_score DECIMAL(5, 2) NOT NULL, -- Algorithmic composite score
    margin_potential_pct DECIMAL(5, 2),       -- Est. Gross Margin %
    competition_barrier_score INTEGER,        -- Review barrier (Lower reviews = easier entry)
    viral_potential_score INTEGER,            -- Fit for TikTok/IG UGC via Fairytales SMM
    
    -- Strategic Assessment
    transatlantic_gap_flag BOOLEAN DEFAULT 0, -- Trending in US, not yet in DE!
    development_verdict VARCHAR(30),          -- 'FAST_TRACK', 'RESEARCH', 'PASS'
    notes TEXT,
    reviewed_by VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (asin, marketplace_id) REFERENCES products(asin, marketplace_id),
    FOREIGN KEY (snapshot_id) REFERENCES weekly_snapshots(snapshot_id)
);

-- Performance Indexes
CREATE INDEX IF NOT EXISTS idx_snapshots_lookup 
ON weekly_snapshots (marketplace_id, category_id, year, week_number, bsr_rank);

CREATE INDEX IF NOT EXISTS idx_opportunities_score 
ON product_opportunities (opportunity_score DESC, development_verdict);
