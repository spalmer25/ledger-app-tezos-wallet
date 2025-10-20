tz4 encoding (in operations)

TOUCH:

 - Show details
 - Blind warning show


<-  test_sign_failing_noop and test_operation_field[message-long-message]  ???

origination and storage


Why !
empty proposals same originate whitelist
increasepaidstorage amount ???





parameter (pair
             (pair ::payload
                (nat ::counter)
                (or ::action
                   (pair ::transfer
                      (mutez ::amount)
                      (contract ::dest unit))
                   (or
                      (option ::delegate key_hash)
                      (pair ::change_keys
                         (nat ::threshold)
                         (list ::keys key)))))
             (list ::sigs (option signature)));

code
  {
    UNPAIR ; SWAP ; DUP ; DIP { SWAP } ;
    DIP
      {
        UNPAIR ;
        DUP ; SELF ; ADDRESS ; CHAIN_ID ; PAIR ; PAIR ;
        PACK ;
        DIP { UNPAIR ::counter ; DIP { SWAP } } ; SWAP
      } ;

    UNPAIR ::stored_counter; DIP { SWAP };
    COMPARE ; EQ ; IF {} {UNIT; FAILWITH} ;

    DIP { SWAP } ; UNPAIR ::threshold ::keys;
    DIP
      {
        PUSH ::valid nat 0; SWAP ;
        ITER
          {
            DIP { SWAP } ; SWAP ;
            IF_CONS
              {
                IF_SOME
                  { SWAP ;
                    DIP
                      {
                        SWAP ; DIP { DIP { DUP } ; SWAP } ;
                        CHECK_SIGNATURE ; IF {} {UNIT; FAILWITH} ;
                        PUSH nat 1 ; ADD ::valid } }
                  { SWAP ; DROP }
              }
              {
                UNIT; FAILWITH
              } ;
            SWAP
          }
      } ;
    COMPARE ; LE ; IF {} {UNIT; FAILWITH} ;
    DROP ; DROP ;

    DIP { UNPAIR ; PUSH nat 1 ; ADD ::new_counter ; PAIR} ;

    NIL operation ; SWAP ;
    IF_LEFT
      {
        UNPAIR ; UNIT ; TRANSFER_TOKENS ; CONS }
      { IF_LEFT {
                  SET_DELEGATE ; CONS }
                {
                  DIP { SWAP ; CAR } ; SWAP ; PAIR ; SWAP }} ;
    PAIR }


type:

    {"prim": "pair", 'args': [
        {"prim": "pair", "annots": [":payload"], 'args': [
            {"prim": "nat", "annots": [":counter"]},
            {"prim": "or", "annots": [":action"], 'args': [
                {"prim": "pair", "annots": [":transfer"], 'args': [
                    {"prim": "mutez", "annots": [":amount"]},
                    {"prim": "contract", "annots": [":dest"], 'args': [{"prim": "unit"}]}
                ]},
                {"prim": "or", 'args': [
                    {"prim": "option", "annots": [":delegate"], 'args': [{"prim": "key_hash"}]},
                    {"prim": "pair", "annots": [":change_keys"], 'args': [
                        {"prim": "nat", "annots": [":threshold"]},
                        {"prim": "list", "annots": [":keys"], 'args': [{"prim": "key"}]}
                    ]}
                ]}
            ]}
        ]},
        {"prim": "list", "annots": [":sigs"], 'args': [{"prim": "option", 'args': [{"prim": "signature"}]}]}
    ]}

Data

    {"prim": "Pair", 'args': [
        {"prim": "Pair", 'args': [
            {"int": 42},
            {"prim": "Left", 'args': [
                {"prim": "Pair", 'args': [
                    {"int": 123456789},
                    {"string": "tz1Ke2h7sDdakHJQh8WX4Z372du1KChsksyU"}
                ]},
            ]},
        ]},
        [{"prim": "Some", 'args': [{"string": "edsigtXomBKi5CTRf5cjATJWSyaRvhfYNHqSUGrn4SdbYRcGwQrUGjzEfQDTuqHhuA8b2d8NarZjz8TRf65WkpQmo423BtomS8Q"}]}, {"prim": "None"}]
    ]}

code
  {
    UNPAIR ; SWAP ; DUP ; DIP { SWAP } ;
    DIP
      {
        UNPAIR ;
        DUP ; SELF ; ADDRESS ; CHAIN_ID ; PAIR ; PAIR ;
        PACK ;
        DIP { UNPAIR @counter ; DIP { SWAP } } ; SWAP
      } ;

    UNPAIR @stored_counter; DIP { SWAP };
    ASSERT_CMPEQ ;

    DIP { SWAP } ; UNPAIR @threshold @keys;
    DIP
      {
        PUSH @valid nat 0; SWAP ;
        ITER
          {
            DIP { SWAP } ; SWAP ;
            IF_CONS
              {
                IF_SOME
                  { SWAP ;
                    DIP
                      {
                        SWAP ; DIIP { DIP { DUP } ; SWAP } ;
                        CHECK_SIGNATURE ; ASSERT ;
                        PUSH nat 1 ; ADD @valid } }
                  { SWAP ; DROP }
              }
              {
                FAIL
              } ;
            SWAP
          }
      } ;
    ASSERT_CMPLE ;
    DROP ; DROP ;

    DIP { UNPAIR ; PUSH nat 1 ; ADD @new_counter ; PAIR} ;

    NIL operation ; SWAP ;
    IF_LEFT
      { UNPAIR ; UNIT ; TRANSFER_TOKENS ; CONS }
      { IF_LEFT {
                  SET_DELEGATE ; CONS }
                {
                  DIP { SWAP ; CAR } ; SWAP ; PAIR ; SWAP }} ;
    PAIR }


