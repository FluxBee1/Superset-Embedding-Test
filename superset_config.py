
# FEATURE_FLAGS = {
#     "EMBEDDED_SUPERSET": True,
# }
# GUEST_TOKEN_JWT_SECRET='Fluxbee'
WTF_CSRF_ENABLED = False


# 1) Turn on Embedded mode
# FEATURE_FLAGS = {"EMBEDDED_SUPERSET": True}

# # 2) Guest token settings (use strong secret + short expiry)
# GUEST_TOKEN_JWT_SECRET = "your-strong-random-secret"
# GUEST_TOKEN_JWT_ALGO = "HS256"
# GUEST_TOKEN_JWT_EXP_SECONDS = 300  # 5 minutes

# # 3) CORS (allow only your front-end origins in prod)
# ENABLE_CORS = True
# CORS_OPTIONS = {
#     "supports_credentials": True,
#     "allow_headers": ["*"],
#     "resources": ["*"],
#     "origins": ["http://localhost:5173"],  # add your real   app origins here
# }



# /root/superset_config.py

# FEATURE_FLAGS = {
#     "EMBEDDED_SUPERSET": True,
# }

# # Guest token settings for embedded SDK
GUEST_TOKEN_JWT_SECRET = "Fluxbee"
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_JWT_EXP_SECONDS = 300  # 5 minutes

# # CORS: allow your front-end origin(s)
# ENABLE_CORS = True
# CORS_OPTIONS = {
#     "supports_credentials": True,
#     "allow_headers": ["*"],
#     "resources": ["*"],
#     "origins": ["http://localhost:5173"],  # add your real app domains in prod
# }

# # (Optional) CSP to allow embedding from your app
# # Prefer CSP frame-ancestors over X-Frame-Options for production
# # TALISMAN_ENABLED = True
# # TALISMAN_CONFIG = {
# #     "content_security_policy": {
# #         "frame-ancestors": ["http://localhost:5173"],
# #     }
# # }

# ==================== SECURITY ====================
# Option A: Disable Talisman
TALISMAN_ENABLED = False

# Option B: Enable with minimal restrictions
# TALISMAN_ENABLED = True
# TALISMAN_CONFIG = {
#     "content_security_policy": None,
#     "frame_options": "ALLOWALL",
# }

# ==================== EMBEDDING ====================
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "EMBEDDED_SUPERSET_UX_BETA": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
}

# ==================== CORS ====================
# ENABLE_CORS = True
# CORS_OPTIONS = {
#     "supports_credentials": True,
#     "allow_headers": ["*"],
#     "resources": ["*"],
#     "origins": ["http://localhost:5173", "http://localhost:3000", "http://localhost:4000"],
# }

# ==================== SESSION ====================
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_HTTPONLY = False  # Allow JavaScript access if needed

# ==================== WTF CSRF ====================
WTF_CSRF_ENABLED = False  # Disable CSRF for APIs

# ==================== PROXY ====================
ENABLE_PROXY_FIX = True

# ==================== OTHER ====================
PUBLIC_ROLE_LIKE = "Gamma"
ENABLE_PROXY_FIX = True
HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}
ENABLE_CORS = True
CORS_OPTIONS = {
"supports_credentials": True,
"allow_headers": ['*'],
"resources": ['*'],
"origins": ['*']
}
OVERRIDE_HTTP_HEADERS = {
    "X-Frame-Options": "ALLOWALL",
}

# ==================== DATABASE ====================
# Your database configuration here
# SQLALCHEMY_DATABASE_URI = 'postgresql://superset:superset@localhost:5432/superset'



