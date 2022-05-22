# This file must be used using `source bin/activate.fish` *within a running fish ( http://fishshell.com ) session*.
# Do not run it directly.

function _bashify_path -d "Converts a fish path to something bash can recognize"
    set fishy_path $argv
    set bashy_path $fishy_path[1]
    for path_part in $fishy_path[2..-1]
        set bashy_path "$bashy_path:$path_part"
    end
    echo $bashy_path
end

function _fishify_path -d "Converts a bash path to something fish can recognize"
    echo $argv | tr ':' '\n'
end

function deactivate -d 'Exit virtualenv mode and return to the normal environment.'
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH"
        # https://github.com/fish-shell/fish-shell/issues/436 altered PATH handling
        if test (echo $FISH_VERSION | head -c 1) -lt 3
            set -gx PATH (_fishify_path "$_OLD_VIRTUAL_PATH")
        else
            set -gx PATH "$_OLD_VIRTUAL_PATH"
        end
        set -e _OLD_VIRTUAL_PATH
    end

    if test -n "$_OLD_VIRTUAL_PYTHONHOME"
        set -gx PYTHONHOME "$_OLD_VIRTUAL_PYTHONHOME"
        set -e _OLD_VIRTUAL_PYTHONHOME
    end

    if test -n "$_OLD_FISH_PROMPT_OVERRIDE"
       and functions -q _old_fish_prompt
        # Set an empty local `$fish_function_path` to allow the removal of `fish_prompt` using `functions -e`.
        set -l fish_function_path

        # Erase virtualenv's `fish_prompt` and restore the original.
        functions -e fish_prompt
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
    end

    set -e VIRTUAL_ENV

    if test "$argv[1]" != 'nondestructive'
        # Self-destruct!
        functions -e pydoc
        functions -e deactivate
        functions -e _bashify_path
        functions -e _fishify_path
    end
end

# Unset irrelevant variables.
deactivate nondestructive

set -gx VIRTUAL_ENV '/home/student/Frank/OpenAPS-Glucosym-3.9/venv'

# https://github.com/fish-shell/fish-shell/issues/436 altered PATH handling
if test (echo $FISH_VERSION | head -c 1) -lt 3
   set -gx _OLD_VIRTUAL_PATH (_bashify_path $PATH)
else
    set -gx _OLD_VIRTUAL_PATH "$PATH"
end
set -gx PATH "$VIRTUAL_ENV"'/bin' $PATH

# Unset `$PYTHONHOME` if set.
if set -q PYTHONHOME
    set -gx _OLD_VIRTUAL_PYTHONHOME $PYTHONHOME
    set -e PYTHONHOME
end

function pydoc
    python -m pydoc $argv
end

if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # Copy the current `fish_prompt` function as `_old_fish_prompt`.
    functions -c fish_prompt _old_fish_prompt

    function fish_prompt
        # Run the user's prompt first; it might depend on (pipe)status.
        set -l prompt (_old_fish_prompt)

        # Prompt override provided?
        # If not, just prepend the environment name.
        if test -n ''
            printf '%s%s' '' (set_color normal)
        else
            printf '%s(%s) ' (set_color normal) (basename "$VIRTUAL_ENV")
        end

        string join -- \n $prompt # handle multi-line prompts
    end

    set -gx _OLD_FISH_PROMPT_OVERRIDE "$VIRTUAL_ENV"
end

# disable nodeenv's prompt
# (prompt already changed by original virtualenv's script)
# https://github.com/ekalinin/nodeenv/issues/26
set NODE_VIRTUAL_ENV_DISABLE_PROMPT 1


# This file must be used with "source bin/activate.fish" *from fish*
# you cannot run it directly

function deactivate_node -d 'Exit nodeenv and return to normal environment.'
    # reset old environment variables
    if test -n "$_OLD_NODE_VIRTUAL_PATH"
        set -gx PATH $_OLD_NODE_VIRTUAL_PATH
        set -e _OLD_NODE_VIRTUAL_PATH
    end

    if test -n "$_OLD_NODE_PATH"
        set -gx NODE_PATH $_OLD_NODE_PATH
        set -e _OLD_NODE_PATH
    else
        set -e NODE_PATH
    end

    if test -n "$_OLD_NPM_CONFIG_PREFIX"
        set -gx NPM_CONFIG_PREFIX $_OLD_NPM_CONFIG_PREFIX
        set -e _OLD_NPM_CONFIG_PREFIX
    else
        set -e NPM_CONFIG_PREFIX
    end

    if test -n "$_OLD_npm_config_prefix"
        set -gx npm_config_prefix $_OLD_npm_config_prefix
        set -e _OLD_npm_config_prefix
    else
        set -e npm_config_prefix
    end

    if test -n "$_OLD_NODE_FISH_PROMPT_OVERRIDE"
        # Set an empty local `$fish_function_path` to allow the removal of
        # `fish_prompt` using `functions -e`.
        set -l fish_function_path

        # Erase virtualenv's `fish_prompt` and restore the original.
        functions -e fish_prompt
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
        set -e _OLD_NODE_FISH_PROMPT_OVERRIDE
    end

    set -e NODE_VIRTUAL_ENV

    if test (count $argv) = 0 -o "$argv[1]" != "nondestructive"
        # Self destruct!
        functions -e deactivate_node
    end
end

function freeze -d 'Show a list of installed packages - like `pip freeze`'
    set -l NPM_VER (npm -v | cut -d '.' -f 1)
    set -l RE "[a-zA-Z0-9\.\-]+@[0-9]+\.[0-9]+\.[0-9]+([\+\-][a-zA-Z0-9\.\-]+)*"

    if test "$NPM_VER" = "0"
        set -g NPM_LIST (npm list installed active >/dev/null ^/dev/null |                          cut -d ' ' -f 1 | grep -v npm)
    else
        set -l NPM_LS "npm ls -g"
        if test (count $argv) -gt 0 -a "$argv[1]" = "-l"
            set NPM_LS "npm ls"
            set -e argv[1]
        end
        set -l NPM_LIST (eval $NPM_LS | grep -E '^.{4}\w{1}' |                                         grep -o -E "$re" |                                         grep -v npm)
    end

    if test (count $argv) = 0
        echo $NPM_LIST
    else
        echo $NPM_LIST > $argv[1]
    end
end

# unset irrelevant variables
deactivate_node nondestructive

# find the directory of this script
begin
    set -l SOURCE (status filename)
    while test -L "$SOURCE"
        set SOURCE (readlink "$SOURCE")
    end
    set -l DIR (dirname (realpath "$SOURCE"))

    # NODE_VIRTUAL_ENV is the parent of the directory where this script is
    set -gx NODE_VIRTUAL_ENV (dirname "$DIR")
end

set -gx _OLD_NODE_VIRTUAL_PATH $PATH
# The node_modules/.bin path doesn't exists and it will print a warning, and
# that's why we redirect stderr to /dev/null :)
set -gx PATH "$NODE_VIRTUAL_ENV/lib/node_modules/.bin" "$NODE_VIRTUAL_ENV/bin" $PATH ^/dev/null

if set -q NODE_PATH
    set -gx _OLD_NODE_PATH $NODE_PATH
    set -gx NODE_PATH "$NODE_VIRTUAL_ENV/lib/node_modules" $NODE_PATH
else
    set -gx NODE_PATH "$NODE_VIRTUAL_ENV/lib/node_modules"
end

if set -q NPM_CONFIG_PREFIX
    set -gx _OLD_NPM_CONFIG_PREFIX $NPM_CONFIG_PREFIX
end
set -gx NPM_CONFIG_PREFIX "$NODE_VIRTUAL_ENV"

if set -q npm_config_prefix
    set -gx _OLD_npm_config_prefix $npm_config_prefix
end
set -gx npm_config_prefix "$NODE_VIRTUAL_ENV"

if test -z "$NODE_VIRTUAL_ENV_DISABLE_PROMPT"
    # Copy the current `fish_prompt` function as `_old_fish_prompt`.
    functions -c fish_prompt _old_fish_prompt

    function fish_prompt
        # Save the current $status, for fish_prompts that display it.
        set -l old_status $status

        # Prompt override provided?
        # If not, just prepend the environment name.
        if test -n "(venv)"
            printf '%s%s ' "(venv)" (set_color normal)
        else
            printf '%s(%s) ' (set_color normal) (basename "$NODE_VIRTUAL_ENV")
        end

        # Restore the original $status
        echo "exit $old_status" | source
        _old_fish_prompt
    end

    set -gx _OLD_NODE_FISH_PROMPT_OVERRIDE "$NODE_VIRTUAL_ENV"
end

set -e NODE_VIRTUAL_ENV_DISABLE_PROMPT
