from mcp.server.fastmcp import FastMCP, Context
from random import choice

from db.user_store import UserStore

# Create an MCP server
mcp = FastMCP("Demo MCP Database Server")

# Add a secret greeting tool
@mcp.tool()
def secret_greeting(name: str) -> str:
    """Provide secret greeting"""
    code = get_random_code()
    return f'Welcome {name}, your secet code is {code}'

# Get codename of users
@mcp.tool()
def get_user_codename(full_name: str, ctx: Context) -> str:
    """Provide user code name"""
    try:
        user = UserStore().get_dbuser_codename(full_name)
        return f'Codename for {full_name} is {user.code_name} and user id is {user.id}'
    except Exception as err:
        ctx.error(str(err))
        return str(err)

# Add user with codename
@mcp.tool()
def add_user_codename(full_name: str, code_name: str, ctx: Context) -> str:
    """Add user with code name"""
    try:
        UserStore().insert_dbuser(full_name, code_name)
        return 'User is added successfully.'
    except Exception as err:
        ctx.error(str(err))
        return str(err)

# Remove User by id
@mcp.tool()
def delete_user(user_id: int, ctx: Context) -> str:
    """Remove user by id"""
    try:
        UserStore().delete_dbuser(user_id)
        return 'User is deleted successfully.'
    except Exception as err:
        ctx.error(str(err))
        return str(err)

def get_random_code():
    mylist = ["ajshkda", "igiwio", "12314"]
    return choice(mylist)