<?php

namespace GuideApp\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * @Entity
 * @Table(name="steps")
 */
class Step
{
    /**
     * @Column(type="integer")
     * @Id
     * @GeneratedValue(strategy="AUTO")
     */
    protected $step_id;
    
    /** @Column(type="string") **/
    protected $type;
    
    /** @Column(type="string") **/
    protected $parameters;
}