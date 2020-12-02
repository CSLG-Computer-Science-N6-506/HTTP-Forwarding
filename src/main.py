import uvicorn
from uvicorn import Config

if __name__ == "__main__":
    uvicorn.run("app:app", headers=[('Server', 'fucking-no-disable-header-option-and-reject-PR-of-it')], reload=True)