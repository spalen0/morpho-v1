methods {
    root() returns address envfree
    initialized() returns bool envfree
    isCreated(address) returns bool envfree
    isWellFormed(address) returns bool envfree
    notEmpty() returns bool envfree
    hash(address) returns bytes32 envfree
    value(address) returns uint256 envfree
}

invariant inializedUnset(address addr)
    ! initialized() => ! isCreated(addr)

invariant wellFormed(address addr)
    isWellFormed(addr)
