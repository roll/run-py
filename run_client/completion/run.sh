_run() 
{
    local list
    local cur

    list=$(run)
    cur=${COMP_WORDS[COMP_CWORD]}

    COMPREPLY=($(compgen -W '${list}' -- $cur))
}

complete -F _run run