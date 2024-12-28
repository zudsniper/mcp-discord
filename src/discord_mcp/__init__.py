"""Discord integration for Model Context Protocol."""

from . import server
import asyncio

__version__ = "0.1.0"

def main():
    """Main entry point for the package."""
    asyncio.run(server.main())

# Expose important items at package level
__all__ = ['main', 'server']