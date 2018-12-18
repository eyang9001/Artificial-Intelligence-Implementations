(define (domain sokorobotto)
  (:requirements :typing)
  (:types  
    shipment order location robot pallette saleitem - object
    robot pallette - bigitem
    )
  (:predicates  (includes ?x - shipment ?y - saleitem)
                (ships ?x - shipment ?y - order)
                (orders ?x - order ?y - saleitem)
                (unstarted ?x - shipment)
                (packing-location ?x - location)
                (available ?x - location)
                (contains ?x - pallette ?y - saleitem)
                (free ?x - robot)
                (connected ?x ?y - location)
                (at ?x - bigitem ?y - location)
                (no-robot ?x - location)
                (no-pallette ?x - location)
                (has ?x - robot ?y - pallette)
                (packing-at ?x - shipment ?y - location)
                (picked-up ?x - pallette)
                (started ?x - shipment)
  )
  (:action robot-move
            :parameters (?robot - robot
                        ?loc1 - location
                        ?loc2 - location)
            :precondition (and (at ?robot ?loc1)
                                (no-robot ?loc2)
                                (connected ?loc1 ?loc2)
                                (free ?robot))
            :effect(and (no-robot ?loc1)
                        (at ?robot ?loc2)
                        (not (at ?robot ?loc1))
                        (not (no-robot ?loc2)))
            )
   (:action robot-move-with-pall
            :parameters (?robot - robot
                        ?loc1 - location
                        ?loc2 - location
                        ?pall - pallette)
            :precondition (and (at ?robot ?loc1)
                                (no-robot ?loc2)
                                (connected ?loc1 ?loc2)
                                (has ?robot ?pall)
                                (no-pallette ?loc2)
                                (at ?pall ?loc1))
            :effect(and (no-robot ?loc1)
                        (at ?robot ?loc2)
                        (at ?pall ?loc2)
                        (not (at ?pall ?loc1))
                        (not (at ?robot ?loc1))
                        (not (no-pallette ?loc2))
                        (no-pallette ?loc1)
                        (not (no-robot ?loc2)))
            )
  (:action robot-pickup
            :parameters (?robot - robot
                        ?loc - location
                        ?pall - pallette
                            )
            :precondition (and (at ?robot ?loc)
                            (at ?pall ?loc)
                            (free ?robot)
                        )
            :effect(and (not(free ?robot))
                        (has ?robot ?pall)
                        (picked-up ?pall)
                        )
                    )
  (:action robot-drop-pack
           :parameters (?robot - robot
                        ?loc - location
                        ?pall - pallette
                        )
           :precondition(and (at ?robot ?loc)
                            (has ?robot ?pall)
                            (picked-up ?pall)
                        )
           :effect(and(not(has ?robot ?pall))
                        (free ?robot)
                        (not(picked-up ?pall))
                        )
                    )
  (:action pack
            :parameters (?loc - location
                        ?pall - pallette
                        ?ship - shipment
                        ?item - saleitem
                        ?order - order)
            :precondition(and 
                            (contains ?pall ?item)
                            (orders ?order ?item)
                            (ships ?ship ?order)
                            (packing-at ?ship ?loc)
                            (packing-location ?loc)
                            (at ?pall ?loc)
                            (started ?ship)
                        )
            :effect(and (includes ?ship ?item)
                        (not (contains ?pall ?item))
                        (not (unstarted ?ship))
                        )
                    )
  (:action begin-packing
            :parameters(?ship - shipment
                        ?loc - location
            )
            :precondition(and(available ?loc)
                            (packing-location ?loc)
            )
            :effect(and (not(available ?loc))
                    (packing-at ?ship ?loc)
                    (started ?ship)
            )
    )
   (:action stop-packing
            :parameters(?loc - location
                        ?ship - shipment
            )
            :precondition(and (packing-location ?loc)
                            (packing-at ?ship ?loc)
            )
            :effect(and (not (packing-at ?ship ?loc))
                        (available ?loc)
            )
  )
)
