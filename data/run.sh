_run() 
{
    local list
    local cur

    list=$(run list -q -s plain=True)
    cur=${COMP_WORDS[COMP_CWORD]}

    COMPREPLY=($(compgen -W '${list}' -- $cur))
}

complete -F _run run